# Generated by Django 4.1.4 on 2022-12-18 16:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0005_alter_customer_state_alter_product_category_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Chandigarh', 'Chandigarh'), ('Gujarat', 'Gujarat'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Rajastan', 'Rajasthan'), ('Karnataka', 'Karnataka'), ('Goa', 'Goa'), ('Telangana', 'Telangana'), ('Assam', 'Assam'), ('Maharashtra', 'Maharashtra'), ('Punjab', 'Punjab'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Andman & Nicobar Islands', 'Andman & Nicobar Islands'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Tamil Nadu', 'Tamil Nadu'), ('Kerala', 'Kerala'), ('Bihar', 'Bihar'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Haryana', 'Haryana'), ('Delhi', 'Delhi'), ('Chattisgarh', 'Chattisgarh'), ('Andra Pradesh', 'Andra Pradesh')], max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('DP', 'Diapering'), ('TY', 'Toys'), ('HS', 'Health & Safety'), ('BP', 'Bath Products'), ('SL', 'School Supplies'), ('NS', 'Nursery Furniture'), ('BY', 'Boy Fashion'), ('FW', 'Footwear'), ('BK', 'Books'), ('GR', 'Gears'), ('GL', 'Girl Fashion'), ('FD', 'Feeding')], max_length=2),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('razorpay_order_id', models.CharField(blank=True, max_length=100, null=True)),
                ('razorpay_payment_status', models.CharField(blank=True, max_length=100, null=True)),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=100, null=True)),
                ('paid', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderPlaced',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('ordered_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('On The Way', 'On The Way'), ('Packed', 'Packed'), ('Accepted', 'Accepted'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel'), ('Pending', 'Pending')], default='Pending', max_length=50)),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.customer')),
                ('payment', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.payment')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
