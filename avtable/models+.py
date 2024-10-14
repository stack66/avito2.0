from django.db import models                                                      
                                                                                  
                                                                                  
class Mavito(models.Model):                                                       
    id = models.CharField(primary_key=True, max_length = 200)                                       
    obj = models.CharField(blank=True, null=True, max_length = 200)                                 
    addr = models.TextField(blank=True, null=True)                                
    region = models.CharField(blank=True, null=True, max_length = 200)                              
    price = models.TextField(blank=True, null=True)  # This field type is a guess.
    m2 = models.CharField(blank=True, null=True, max_length = 200)                                  
    floor = models.CharField(blank=True, null=True, max_length = 200)                               
    floors = models.CharField(blank=True, null=True, max_length = 200)                              
    links = models.CharField(blank=True, null=True, max_length = 200)                               
    descr = models.TextField(blank=True, null=True)                               
    date = models.DateTimeField(blank=True, null=True)                            
    date1 = models.DateTimeField(blank=True, null=True)                           
    last_updated = models.TextField(blank=True, null=True)                        
    tel = models.CharField(blank=True, null=True, max_length = 200)                                 
    linkimg = models.CharField(blank=True, null=True, max_length = 200)                             
    lastrowid = models.IntegerField(blank=True, null=True)                        
    agent = models.IntegerField()                                                 
                                                                                  
    class Meta:                                                                   
        managed = False                                                           
        db_table = 'mavito'                                                       
