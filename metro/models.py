from django.db import models

# class Line(models.Model):
    # id_line = models.AutoField(primary_key=True, verbose_name = 'ID')
    # name_line = models.CharField(max_length=255,verbose_name='Линия метро',unique=True)    

    # class Meta:
        # db_table = 'Line'
        # verbose_name = 'Линию'
        # verbose_name_plural = 'Линии'
       	

    # def __str__(self):
        # return self.name_line   

class Station(models.Model):
    id = models.AutoField(primary_key=True, verbose_name = 'ID')
    name_station = models.CharField(max_length=255,verbose_name='Название станции')
    id_line = models.CharField(max_length=255,verbose_name='ID линии')
    name_line = models.CharField(max_length=255,verbose_name='Линия метро') 

    # line = models.ForeignKey(Line,blank=True, null=True, to_field='name_line', on_delete=models.CASCADE,verbose_name='Линия метро')

    class Meta:
        db_table = 'Station'
        verbose_name = 'Станцию'
        verbose_name_plural = 'Станции'
       	

    # def __str__(self):
        # return self.name_station
    

class Stationtime(models.Model):
    id_st_time = models.AutoField(primary_key=True, verbose_name = 'ID')
   # st_1 = models.ForeignKey(Station,blank=True, null=True, to_field='name_station', on_delete=models.CASCADE,verbose_name='Станция отправления',related_name='st_transfer_1')
   # st_2 = models.ForeignKey(Station,blank=True, null=True, to_field='name_station', on_delete=models.CASCADE,verbose_name='Станция прибытия',related_name='st_transfer_2')
    st_time = models.IntegerField(verbose_name='Время в пути',blank=True, null=True)

    class Meta:
        db_table = 'Stationtime'
        verbose_name = 'Время прибития'
        verbose_name_plural = 'Время прибития'
       	

class Transfertime(models.Model):
    id_t_time = models.AutoField(primary_key=True, verbose_name = 'ID')
  #  tr_1 = models.ForeignKey(Station,blank=True, null=True, to_field='name_station', on_delete=models.CASCADE,verbose_name='Станция пересадки 1',related_name='transfer_1')
   # tr_2 = models.ForeignKey(Station,blank=True, null=True, to_field='name_station', on_delete=models.CASCADE,verbose_name='Станция пересадки 2',related_name='transfer_2')
    transfer_time = models.IntegerField(verbose_name='Время в пути')

    class Meta:
        db_table = 'Transfertime'
        verbose_name = 'Время пересадки'
        verbose_name_plural = 'Время пересадки'
       	

