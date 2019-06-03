# Generated by Django 2.1.4 on 2019-06-02 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gateway', '0006_auto_20190531_2207'),
        ('devices', '0002_auto_20190531_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='RTU_device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_name', models.CharField(max_length=20)),
                ('slave_id', models.IntegerField()),
                ('description', models.TextField(default='', max_length=200, verbose_name='设备描述')),
                ('create_time', models.DateField()),
                ('baud_rate', models.IntegerField(default=9600)),
                ('bite_size', models.IntegerField(default=8)),
                ('parity', models.CharField(default='N', max_length=1)),
                ('stopbits', models.FloatField(default=1)),
                ('protocol_way', models.CharField(max_length=3, verbose_name='设备接入方式')),
                ('last_active', models.DateField(auto_now=True)),
                ('gateway_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gateway.GatewayBase')),
            ],
        ),
    ]
