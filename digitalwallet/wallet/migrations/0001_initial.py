# Generated by Django 4.0.6 on 2022-08-01 19:24

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_type', models.CharField(max_length=15, null=True)),
                ('balance', models.PositiveIntegerField()),
                ('account_name', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('origin_county', models.CharField(max_length=25, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('phoneneumber', models.CharField(max_length=10)),
                ('age', models.PositiveSmallIntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('pin', models.CharField(max_length=8, null=True)),
                ('id_number', models.CharField(max_length=10, null=True)),
                ('nationality', models.CharField(max_length=20, null=True)),
                ('occupation', models.CharField(max_length=10, null=True)),
                ('signature', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_type', models.CharField(max_length=15, null=True)),
                ('receipt_date', models.DateField(default=django.utils.timezone.now)),
                ('receipt_file', models.FileField(upload_to='')),
                ('total_amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField()),
                ('date_created', models.DateTimeField()),
                ('pin', models.CharField(max_length=8, null=True)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Wallet_currency', to='wallet.currency')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Wallet_customer', to='wallet.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_amount', models.IntegerField()),
                ('transaction_type', models.CharField(max_length=15, null=True)),
                ('transaction_charge', models.IntegerField()),
                ('transaction_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('destination_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Transaction_destination_account', to='wallet.account')),
                ('origin_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Transaction_receipt', to='wallet.account')),
                ('receipt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Transaction_receipt', to='wallet.receipt')),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Transaction_wallet', to='wallet.wallet')),
            ],
        ),
        migrations.CreateModel(
            name='Thirdparty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, null=True)),
                ('thirdparty_id', models.IntegerField()),
                ('phone_number', models.IntegerField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Thirdparty_account', to='wallet.account')),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_and_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('customer_id', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('bonus', models.IntegerField()),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Reward_transaction', to='wallet.transaction')),
            ],
        ),
        migrations.AddField(
            model_name='receipt',
            name='transaction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Receipt_transaction', to='wallet.transaction'),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notifications_id', models.IntegerField()),
                ('name', models.CharField(max_length=15, null=True)),
                ('status', models.CharField(max_length=15, null=True)),
                ('date_and_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('receipt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Notifications_receipt', to='wallet.receipt')),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_number', models.IntegerField()),
                ('loan_type', models.CharField(max_length=15, null=True)),
                ('amount', models.IntegerField()),
                ('date_and_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('interest_rate', models.IntegerField()),
                ('pay_due_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('loan_balance', models.IntegerField()),
                ('guarantor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Loan_guarantor', to='wallet.customer')),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Loan_wallet', to='wallet.wallet')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_issued', models.DateTimeField(default=django.utils.timezone.now)),
                ('card_name', models.CharField(max_length=15, null=True)),
                ('card_number', models.IntegerField()),
                ('card_type', models.CharField(max_length=15, null=True)),
                ('exipry_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('card_status', models.CharField(max_length=15, null=True)),
                ('security_code', models.IntegerField()),
                ('signature', models.ImageField(upload_to='')),
                ('issuer', models.CharField(max_length=15, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Card_account', to='wallet.account')),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Card_wallet', to='wallet.wallet')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='wallet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Account_wallet', to='wallet.wallet'),
        ),
    ]