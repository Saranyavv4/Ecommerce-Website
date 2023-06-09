# Generated by Django 4.1.4 on 2022-12-18 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_customer_state_alter_product_category_payment_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderplaced',
            old_name='Customer',
            new_name='customer',
        ),
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Assam', 'Assam'), ('Delhi', 'Delhi'), ('Haryana', 'Haryana'), ('Punjab', 'Punjab'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Gujarat', 'Gujarat'), ('Telangana', 'Telangana'), ('Bihar', 'Bihar'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Andra Pradesh', 'Andra Pradesh'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Rajastan', 'Rajasthan'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Tamil Nadu', 'Tamil Nadu'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Chattisgarh', 'Chattisgarh'), ('Goa', 'Goa'), ('Maharashtra', 'Maharashtra'), ('Chandigarh', 'Chandigarh'), ('Andman & Nicobar Islands', 'Andman & Nicobar Islands')], max_length=100),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('On The Way', 'On The Way'), ('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Packed', 'Packed'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel')], default='Pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('DP', 'Diapering'), ('TY', 'Toys'), ('HS', 'Health & Safety'), ('BY', 'Boy Fashion'), ('FW', 'Footwear'), ('GL', 'Girl Fashion'), ('BP', 'Bath Products'), ('NS', 'Nursery Furniture'), ('GR', 'Gears'), ('BK', 'Books'), ('FD', 'Feeding'), ('SL', 'School Supplies')], max_length=2),
        ),
    ]
