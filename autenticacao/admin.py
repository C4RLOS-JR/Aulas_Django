from django.contrib import admin
from .models import Pessoa, Cargos, Pedido


class PedidoInline(admin.TabularInline):
  list_display = ('nome', 'quantidade', 'descricao')
  readonly_fields = ('nome', 'quantidade', 'descricao')
  extra = 0
  model = Pedido


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
  inlines = [PedidoInline]
  list_display = ('nome', 'email', 'cargo')
  list_filter = ('cargo',)
  list_editable = ('email',)
  search_fields = ('nome',)
  readonly_fields = ('senha',)

admin.site.register(Cargos)