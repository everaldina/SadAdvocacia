from django.shortcuts import render

from sad_app.models import Publicacao, tipoPublicacao, Cargo
from django.contrib.auth.models import Group
from sad_app.forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.hashers import make_password
from django.apps import apps
from django.contrib.auth.models import User, Permission
from django.db.models.deletion import ProtectedError

# Create your views here.
def context_(request):
    context = {
        'user': request.user,
    }

    return context

def home(request):
    cargos = Cargo.objects.all()
    equipe_por_cargo = {}
    
    for cargo in cargos:
        equipe_por_cargo[cargo] = cargo.membro_set.all()
        
    for cargo in equipe_por_cargo:
        for membro in equipe_por_cargo[cargo]:
            membro.formacao_ordenadas = membro.formacao_set.all().order_by('ano_entrada')

    context = {
        'equipe_por_cargo': equipe_por_cargo
    }

    return render(request, 'index.html', context)


def cadastro_usuario(request):
    if request.method == "GET":
        form_cadastro = CadastroUsuarioForm()

        context = {
            'form_cadastro_usuario': form_cadastro,
        }

        return render(request, 'cadastro-usuario.html', context=context)
    
    if request.method == "POST":
        request_data = request.POST.copy()
        request_data['password'] = make_password(request_data['password'])
        form_cadastro = CadastroUsuarioForm(request_data)

        if form_cadastro.is_valid():
            form_cadastro.save()

            return HttpResponseRedirect(reverse('login'))

        form_cadastro.add_error(None, 'Erro ao cadastrar usuário')

        context = {
            'form_cadastro_usuario': form_cadastro,
        }

        return render(request, 'cadastro-usuario.html', context=context)
    
def login(request):
    if request.method == "GET":
        form_login = LoginForm()

        context = {
            'form_login': form_login,
        }

        return render(request, 'login.html', context=context)
    
    if request.method == "POST":
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        
        if user:
            auth_login(request, user)
            return HttpResponseRedirect(reverse('home'))
        
        form_login = LoginForm(request.POST)

        form_login.add_error(None, ['Usuário ou senha inválidos'])

        context = {
            'form_login': form_login,
        }
        
        return render(request, 'login.html', context=context)
    
def logout(request):
    auth_logout(request)

    return HttpResponseRedirect(reverse('login'))

def publicacoes(request):    
    tipoLivro = tipoPublicacao.objects.get(nome = 'Livro')
    livros = Publicacao.objects.filter(fk_tipo=tipoLivro.id).order_by('data_publicacao')
    
    tipoArtigo = tipoPublicacao.objects.get(nome = 'Artigo Científico')
    artigos = Publicacao.objects.filter(fk_tipo=tipoArtigo.id).order_by('data_publicacao')
    
    context = {
        'livros': livros,
        'artigos': artigos,
    }
    
    return render(request, 'publicacoes.html', context)

def contato(request):
    if request.method == "POST":    
        form = ContatoForm()
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("contato"))
    else:
        form = ContatoForm()

    if request.method == 'POST':
        form = ContatoForm(request.POST)

        if form.is_valid():
            form.save()
            form = ContatoForm()

    context = {
        'form': form,
    }
    
    return render(request, 'contato.html', context)

def formulario_membro(request):
    user = request.user

    if not user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    
    if request.method == "POST":
        form_membro = MembroForm(request.POST)
        if form_membro.is_valid():
            form_membro.save()
            return HttpResponseRedirect(reverse('formulario_membro'))
    else:
        form_membro = MembroForm()

    context = {
        'form_membro': form_membro,
    }

    return render(request, 'forms/membro.html', context=context)

def formulario_publicacao(request):
    user = request.user

    if not user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    
    if request.method == "POST":
        form_publicacao = PublicacaoForm(request.POST)
        if form_publicacao.is_valid():
            form_publicacao.save()
            return HttpResponseRedirect(reverse("formulario_publicacao"))
    form_publicacao = PublicacaoForm()
    
    context = {
        'form_publicacao': form_publicacao,
    }
    
    return render(request, 'forms/publicacao.html', context)

def formulario_tipoPublicacao(request):
    user = request.user

    if not user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    
    if request.method == 'POST':
        form_tipo_publicacao = TipoPublicacaoForm(request.POST)
        if form_tipo_publicacao.is_valid():
            form_tipo_publicacao.save()
            return HttpResponseRedirect(reverse('formulario_tipo_publicacao'))
    else: 
        form_tipo_publicacao = TipoPublicacaoForm()
        
    
    context = {
        'form_tipo_publicacao': form_tipo_publicacao,
    }

    return render(request, 'forms/tipo_publicacao.html', context)

def formulario_formacao(request):
    user = request.user

    if not user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    
    if request.method == 'POST':
        form_formacao = FormacaoForm(request.POST)
        if form_formacao.is_valid():
            form_formacao.save()
            return HttpResponseRedirect(reverse('formulario_formacao'))
    else:
        form_formacao = FormacaoForm()
        

    context = {
        'form_formacao': form_formacao,
    }

    return render(request, 'forms/formacao.html', context=context)

def formulario_nacionalidade(request):
    user = request.user

    if not user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    
    if request.method == "POST":
        form_nacionalidade = NacionalidadeForm(request.POST)
        if form_nacionalidade.is_valid():
            form_nacionalidade.save()
            return HttpResponseRedirect(reverse("formulario_nacionalidade"))
    form_nacionalidade = NacionalidadeForm()

    context = {
        'form_nacionalidade': form_nacionalidade,
    }

    return render(request, 'forms/nacionalidade.html', context)

def formulario_cargo(request):
    user = request.user

    if not user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    
    if request.method == 'POST':
        form_cargo = CargoForm(request.POST)
        if form_cargo.is_valid():
            form_cargo.save()
            return HttpResponseRedirect(reverse('formulario_cargo'))
    else:
        form_cargo = CargoForm()

    context = {
        'form_cargo': form_cargo,
    }

    return render(request, 'forms/cargo.html', context)

def formulario_instituicao(request):
    user = request.user

    if not user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    
    if request.method == 'POST':
        form_instituicao = InstituicaoForm(request.POST)
        if form_instituicao.is_valid():
            form_instituicao.save()
            return HttpResponseRedirect(reverse('formulario_instituicao'))
    else:
        form_instituicao = InstituicaoForm()

    context = {
        'form_instituicao': form_instituicao,
    }

    return render(request, 'forms/instituicao.html', context)

def formulario_curso(request):
    user = request.user

    if not user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    
    if request.method == 'POST':
        form_curso = CursoForm(request.POST)
        if form_curso.is_valid():
            form_curso.save()
            return HttpResponseRedirect(reverse('formulario_curso'))
    else:
        form_curso = CursoForm()

    context = {
        'form_curso': form_curso,
    }

    return render(request, 'forms/curso.html', context)

def formulario_modalidade(request):
    user = request.user

    if not user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    
    if request.method == 'POST':
        form_modalidade = ModalidadeForm(request.POST)
        if form_modalidade.is_valid():
            form_modalidade.save()
            return HttpResponseRedirect(reverse('formulario_modalidade'))
    else:
        form_modalidade = ModalidadeForm()

    context = {
        'form_modalidade': form_modalidade,
    }

    return render(request, 'forms/modalidade.html', context)

def formulario_nivel_formacao(request):
    user = request.user

    if not user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    
    if request.method == "POST":
        form_nivel = NivelFormacaoForm(request.POST)
        if form_nivel.is_valid():
            form_nivel.save()
            return HttpResponseRedirect(reverse('formulario_nivelformacao'))
    else:
        form_nivel = NivelFormacaoForm()
    
    context = {
        'form_nivel': form_nivel,
    }

    return render(request, 'forms/nivel.html', context)

def formulario_grupo(request):
    user = request.user

    if not user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    
    if request.method == 'POST':
        form_grupo = GrupoForm(request.POST)
        if form_grupo.is_valid():
            form_grupo.save()
            return HttpResponseRedirect(reverse('formulario_grupo'))

    form_grupo = GrupoForm()

    context = {
        'form_grupo': form_grupo,
    }

    return render(request, 'forms/grupo.html', context)

def cadastro(request):
    return render(request, 'forms/membro.html')

def perfil(request):
    user = request.user

    if not user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    
    user_form = CadastroUsuarioForm(instance=user)

    context = {
        'user_form': user_form,
    }
    
    return render(request, 'perfil.html', context=context)

def editar_perfil(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)

        request_copy = request.POST.copy()

        request_copy['password'] = user.password

        user_form = CadastroUsuarioForm(data=request_copy, instance=user)

        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('perfil'))
        
        context = {
            'user_form': user_form,
        }
        
        return render(request, 'perfil.html', context=context)

    return HttpResponseRedirect(reverse('perfil'))

def encerrar_conta(request):
    # request.user.delete()
    request.user.is_active = False

    auth_logout(request)

    return HttpResponseRedirect(reverse('login'))

def lista_modelo(request, tabela):
    user = request.user

    if not user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    
    if not user.is_staff:
        return HttpResponseRedirect(reverse('home'))
    
    context = context_(request)
    
    if tabela != 'usuario':
        nome = "sad_app_" + tabela
        link = "formulario_" + tabela
    else:
        nome = "auth_user"
        link = "cadastro_usuario"
    model_list = {}
    model_list['usuario'] = 'Usuário'
    model_list['grupo'] = 'Grupo'
    model = None
    for m in apps.get_models():
        nome_tabela = m._meta.db_table
        if nome_tabela.startswith("sad_app") and not nome_tabela.endswith("usuario"):
            model_list["".join(nome_tabela.split("_")[2:])] = m._meta.verbose_name.capitalize()
        if nome_tabela == nome or nome_tabela == 'auth_group':
            model = m
            
    registros = model.objects.all()
    context['registros'] = registros
    context['add'] = 'formulario_' + tabela
    context['lista_modelos'] = model_list
    context['link'] = link
    
    if request.method == "POST":
        list_delete = []
        for key in request.POST:
            if key != "csrfmiddlewaretoken":
                list_delete.append(request.POST[key])
        
        try:
            # deleta os registros   
            count_delete, model_deletions = model.objects.filter(id__in=list_delete).delete()
        # exesçao para registros protegidos    
        except ProtectedError as e: 
            tabelas_protegidos = []
            itens_protegidos = []
            for item in e.protected_objects:
                if item.__class__.__name__ not in tabelas_protegidos:
                    tabelas_protegidos.append(item.__class__.__name__)
                itens_protegidos.append(item)
            context['itens_protegidos'] = itens_protegidos
            context['tabelas_protegidos'] = tabelas_protegidos
            return render(request, 'admin/lista_modelo.html', context)
        
        context['count_delete'] = count_delete
        context['model_deletions'] = model_deletions
        
    return render(request, 'admin/lista_modelo.html', context)
    
def painel_admin(request):
    user = request.user

    if not user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    
    if not user.is_staff:
        return HttpResponseRedirect(reverse('home'))
    
    context = context_(request)

    model_list = {}
    model_list['usuario'] = 'Usuário'
    model_list['grupo'] = 'Grupo'

    for m in apps.get_models():
        nome_tabela = m._meta.db_table
        if nome_tabela.startswith("sad_app") and not nome_tabela.endswith("usuario"):
            model_list["".join(nome_tabela.split("_")[2:])] = m._meta.verbose_name.capitalize()
    
    context['lista_modelos'] = model_list

    return render(request, 'admin/lista.html', context=context)


def editar_registro(request, tabela, id):
    context = {}
    if request.method == "GET":
        if tabela == 'usuario':
            nome = "auth_user"
        elif tabela == 'grupo':
            nome = "auth_group"
        else:
            nome = "sad_app_" + tabela
            
        model_list = {}
        model_list['usuario'] = 'Usuário'
        model_list['grupo'] = 'Grupo'
        model = None
        for m in apps.get_models():
            nome_tabela = m._meta.db_table
            if nome_tabela.startswith("sad_app") and not nome_tabela.endswith("usuario"):
                model_list["".join(nome_tabela.split("_")[2:])] = m._meta.verbose_name.capitalize()
            elif nome_tabela == 'auth_user':
                model_list['usuario'] = 'Usuário'
            if nome_tabela == nome or nome_tabela == 'auth_group':
                model = m
        
        registro = model.objects.get(id=id)
        form = None
        if tabela == "membro":
            form = MembroForm(instance=registro)
        elif tabela == "publicacao":
            form = PublicacaoForm(instance=registro)
        elif tabela == "tipopublicacao":
            form = TipoPublicacaoForm(instance=registro)
        elif tabela == "formacao":
            form = FormacaoForm(instance=registro)
        elif tabela == "nacionalidade":
            form = NacionalidadeForm(instance=registro)
        elif tabela == "cargo":
            form = CargoForm(instance=registro)
        elif tabela == "instituicao":
            form = InstituicaoForm(instance=registro)
        elif tabela == "curso":
            form = CursoForm(instance=registro)
        elif tabela == "nivelformacao":
            form = NivelFormacaoForm(instance=registro)
        elif tabela == "modalidade":
            form = ModalidadeForm(instance=registro)
        elif tabela == "contato":
            form = ContatoForm(instance=registro)
        elif tabela == "usuario":
            usuario = Usuario.objects.filter(user_ptr_id=id)
            
            if len(usuario) != 0:
                registro = usuario[0]
                
            form = CadastroUserForm(instance = registro)
            context['is_superuser'] = registro.is_superuser
            context['is_staff'] = registro.is_staff
            
            permissao_usuario = []
            for permissao in registro.user_permissions.all():
                permissao_usuario.append(permissao.id)
                
            permissioes_agrupadas = get_permissions_grouped()
            context['permissoes'] = permissioes_agrupadas
            context['permissao_usuario'] = permissao_usuario
            context['mode'] = 'user'
            context['grupos'] = Group.objects.all()
            context['grupos_usuario'] = registro.groups.all()
            
            print(permissao_usuario)
        elif tabela == "grupo":
            form = GrupoForm(instance=registro)
            permissioes_agrupadas = get_permissions_grouped()
            
            permissao_grupo = []
            for permissao in registro.permissions.all():
                permissao_grupo.append(permissao.id)
                
            context['permissoes'] = permissioes_agrupadas
            context['permissao_grupo'] = permissao_grupo
            context['mode'] = 'group'
            
            
            
        context['form']  = form
        context['tabela']  = tabela
        context['id']  = id
        context['lista_modelos']  = model_list
        
        return render(request, 'admin/editar_registro.html', context)

    if request.method == "POST":
        form = None
        registro = None

        if tabela == "membro":
            registro = Membro.objects.get(id=id)
            form = MembroForm(request.POST, instance=registro)
        elif tabela == "publicacao":
            registro = Publicacao.objects.get(id=id)
            form = PublicacaoForm(request.POST, instance=registro)
        elif tabela == "tipoPublicacao":
            registro = tipoPublicacao.objects.get(id=id)
            form = TipoPublicacaoForm(request.POST, instance=registro)
        elif tabela == "formacao":
            registro = Formacao.objects.get(id=id)
            form = FormacaoForm(request.POST, instance=registro)
        elif tabela == "nacionalidade":
            registro = Nacionalidade.objects.get(id=id)
            form = NacionalidadeForm(request.POST, instance=registro)
        elif tabela == "cargo":
            registro = Cargo.objects.get(id=id)
            form = CargoForm(request.POST, instance=registro)
        elif tabela == "instituicao":
            registro = Instituicao.objects.get(id=id)
            form = InstituicaoForm(request.POST, instance=registro)
        elif tabela == "curso":
            registro = Curso.objects.get(id=id)
            form = CursoForm(request.POST, instance=registro)
        elif tabela == "nivel_formacao":
            registro = NivelFormacao.objects.get(id=id)
            form = NivelFormacaoForm(request.POST, instance=registro)
        elif tabela == "modalidade":
            registro = Modalidade.objects.get(id=id)
            form = ModalidadeForm(request.POST, instance=registro)
        elif tabela == "contato":
            registro = Contato.objects.get(id=id)
            form = ContatoForm(request.POST, instance=registro)
        elif tabela == "grupo":
            registro = Group.objects.get(id=id)

            form = GrupoForm(request.POST, instance=registro)

            permlist = []
            for permissao in request.POST.getlist("permissoes"):
                permlist.append(Permission.objects.get(id=permissao))

            grupo = form.save(commit=False)
            grupo.save()

            grupo.permissions.set(permlist)
        elif tabela == "usuario":
            usuario = Usuario.objects.filter(user_ptr_id=id)
            
            if len(usuario) != 0:
                registro = usuario[0]
            
            form = CadastroUserForm(request.POST, instance=registro)
            context['is_superuser'] = registro.is_superuser
            context['is_staff'] = registro.is_staff
            
            permlist = []
            for permissao in request.POST.getlist("permissoes"):
                permlist.append(Permission.objects.get(id=permissao))
            
            grouplist = []
            for grupo in request.POST.getlist("grupos"):
                grouplist.append(Group.objects.get(id=grupo))

            user = form.save(commit=False)
            user.save()

            user.user_permissions.set(permlist)
            user.user_groups.set(grouplist)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('lista_modelo', args=[tabela]))
        
def excluir_registro(request, tabela, id):
    if tabela == 'usuario':
            nome = "auth_user"
    elif tabela == 'grupo':
        nome = "auth_group"
    else:
        nome = "sad_app_" + tabela

    model = None
    for m in apps.get_models():
        nome_tabela = m._meta.db_table
        if nome_tabela == nome:
            model = m
    
    model.objects.filter(id=id).delete()
    
    return HttpResponseRedirect(reverse('lista_modelo', args=[tabela]))


def get_permissions_grouped():
    permissions = Permission.objects.all()
    permissions_grouped = {}
    
    for permission in permissions:
        nome_permissao = permission.codename.split("_")
        if nome_permissao[1] not in permissions_grouped:
            permissions_grouped[nome_permissao[1]] = {nome_permissao[0]: permission}
        else:
            permissions_grouped[nome_permissao[1]][nome_permissao[0]] = permission
    return permissions_grouped