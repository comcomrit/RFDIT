# Generated by Django 3.1.2 on 2020-10-14 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0009_auto_20201009_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplies_fict',
            name='status_sup',
            field=models.IntegerField(choices=[(0, 'ดี'), (1, 'ชำรุด'), (2, 'รอจำหน่าย'), (3, 'จำหน่ายแล้ว')], default=0, max_length=100, verbose_name='สถานะ'),
        ),
        migrations.AlterField(
            model_name='supplies_fict',
            name='supplies_type',
            field=models.IntegerField(choices=[(0, 'คอมพิวเตอร์ตั้งโต๊ะ'), (1, 'คอมพิวเตอร์โน๊ตบุ๊ค'), (2, 'เครื่องสำรองไฟ UPS'), (3, 'เครื่องพิมพ์ ขาวดำ LED'), (4, 'เครื่องพิมพ์ สี LED'), (5, 'เครื่องสแกน Scanner'), (6, 'เครื่องพิมพ์ฉีดหมึก Ink jet'), (7, 'Scanner'), (8, 'เครื่องพิมพ์ Multifunction'), (9, 'คอมพิวเตอร์แท็ปแล็ต Tablet'), (10, 'เครื่องพิมพ์แผนที่ plotter')], default=0, max_length=100, verbose_name='รายการครุภัณฑ์'),
        ),
    ]
