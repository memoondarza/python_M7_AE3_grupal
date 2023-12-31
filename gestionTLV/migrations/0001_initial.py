# Generated by Django 4.2.4 on 2023-08-16 21:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id_cliente', models.CharField(default='999999', max_length=6, primary_key=True, serialize=False)),
                ('nombre_cliente', models.CharField(max_length=30)),
                ('apellidos_cliente', models.CharField(max_length=30)),
                ('direccion_cliente', models.CharField(max_length=60)),
                ('ciudad_cliente', models.CharField(max_length=30)),
                ('comuna_cliente', models.CharField(max_length=30)),
                ('sector_cliente', models.CharField(max_length=30)),
                ('telefono_cliente', models.CharField(max_length=12)),
                ('correo_cliente', models.EmailField(max_length=40)),
                ('password_cliente', models.CharField(max_length=8)),
                ('crea_cliente', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id_pedido', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('fecha_pedido', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecha_entrega', models.DateTimeField(default=django.utils.timezone.now)),
                ('estado_pedido', models.CharField(choices=[('1', 'Pendiente'), ('2', 'En preparación'), ('3', 'En despacho'), ('4', 'Entregado')], default='1', max_length=1)),
                ('forma_pago', models.CharField(choices=[('1', 'Contado, T.Debito'), ('2', 'Por T.Crédito 1 cuota'), ('3', 'Por T.Crédito 3 cuotas'), ('4', 'Por T.Crédito 6 cuotas'), ('5', 'Por T.Crédito 12 cuotas'), ('6', 'Por T.Crédito 24 cuotas')], default='1', max_length=1)),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionTLV.clientes')),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id_producto', models.CharField(default='100000', max_length=6, primary_key=True, serialize=False)),
                ('nombre_producto', models.CharField(max_length=60)),
                ('marca_producto', models.CharField(max_length=30)),
                ('unidad_producto', models.CharField(max_length=20)),
                ('categoria_producto', models.CharField(choices=[('1', 'Zapatillas deportivas'), ('2', 'Zapatillas urbanas'), ('3', 'Ropa deportiva'), ('4', 'Implementos deportivos'), ('5', 'Máquinas de ejercicios'), ('6', 'Otras categorías')], default='1', max_length=1)),
                ('stock_producto', models.IntegerField()),
                ('precio_producto', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RelacionPedidosProductos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_pedido', models.IntegerField()),
                ('id_pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionTLV.pedidos')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionTLV.productos')),
            ],
        ),
    ]
