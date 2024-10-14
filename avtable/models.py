from django.db import models                                                      
                                                                                  
                                                                                  
class Mavito(models.Model):                                                       
    id = models.CharField(primary_key=True, max_length = 30)                                       
    obj = models.CharField(blank=True, null=True, max_length = 80)                                 
    addr = models.TextField(blank=True, null=True, max_length = 80)                                
    region = models.CharField(blank=True, null=True, max_length = 80)                              
    price = models.IntegerField(blank=True, null=True)  # This field type is a guess.
    m2 = models.CharField(blank=True, null=True, max_length = 10)                                  
    floor = models.CharField(blank=True, null=True, max_length = 3)                               
    floors = models.CharField(blank=True, null=True, max_length = 3)                              
    links = models.CharField(blank=True, null=True, max_length = 80)                               
    descr = models.TextField(blank=True, null=True)                               
    date = models.DateTimeField(blank=True, null=True)                            
    date1 = models.DateTimeField(blank=True, null=True)                           
    last_updated = models.TextField(blank=True, null=True)                        
    tel = models.CharField(blank=True, null=True, max_length = 12)                                 
    linkimg = models.CharField(blank=True, null=True, max_length = 200)                             
    agent = models.IntegerField()

                                                                                  
    class Meta:                                                                   
        managed = False                                                           
        db_table = 'mavito'

class Mavhouse(models.Model):                                                     
    id = models.CharField(primary_key=True, max_length = 30)                                       
    obj = models.CharField(blank=True, null=True, max_length = 80)                                 
    addr = models.CharField(blank=True, null=True, max_length = 80)                                
    region = models.CharField(blank=True, null=True, max_length = 80)                              
    price = models.IntegerField(blank=True, null=True)  # This field type is a guess.
    m2 = models.CharField(blank=True, null=True, max_length = 10)                                  
    floor = models.CharField(blank=True, null=True, max_length = 3)                               
    floors = models.CharField(blank=True, null=True, max_length = 3)                              
    links = models.CharField(blank=True, null=True, max_length = 80)                               
    descr = models.TextField(blank=True, null=True)                               
    date = models.DateTimeField(blank=True, null=True)                            
    date1 = models.DateTimeField(blank=True, null=True)                           
    last_updated = models.CharField(blank=True, null=True, max_length = 20)                        
    tel = models.CharField(blank=True, null=True, max_length = 12)                                 
    linkimg = models.CharField(blank=True, null=True, max_length = 200)                             
    agent = models.IntegerField()
    class Meta:                                                                   
        managed = False                                                           
        db_table = 'mavhouse'

class Region(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(blank=True, null=True, max_length = 20)

    class Meta:                                                                   
        managed = False                                                           
        db_table = 'region'
class Street(models.Model):
    id = models.IntegerField(primary_key=True)                         
    reg_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(blank=True, null=True, max_length = 80)  
                                                    
    class Meta:                                     
        managed = False                             
        db_table = 'street'                         
class Youkv(models.Model):                                                        
    id = models.CharField(primary_key=True, max_length = 30)                                       
    obj = models.CharField(blank=True, null=True, max_length = 80)                                 
    floor = models.CharField(blank=True, null=True, max_length = 3)                               
    floors = models.CharField(blank=True, null=True, max_length = 3)                              
    m2 = models.CharField(blank=True, null=True, max_length = 10)                                  
    region = models.CharField(blank=True, null=True, max_length = 80)                              
    addr = models.CharField(blank=True, null=True, max_length = 80)                                
    price = models.IntegerField(blank=True, null=True)  # This field type is a guess.
    links = models.CharField(blank=True, null=True, max_length = 80)                       
    descr = models.TextField(blank=True, null=True)                               
    date = models.DateTimeField(blank=True, null=True)                            
    date1 = models.DateTimeField(blank=True, null=True)                           
    last_updated = models.CharField(blank=True, null=True, max_length = 20)                        
    tel = models.CharField(blank=True, null=True, max_length = 12)                                 
    linkimg = models.CharField(blank=True, null=True, max_length = 200)                             
    agent = models.IntegerField()                                                 
                                                                                  
    class Meta:                                                                   
        managed = False                                                           
        db_table = 'youkv'

class Flat(models.Model):                                 
    id = models.CharField(primary_key=True, max_length = 30)          
    obj = models.CharField(blank=True, null=True, max_length = 80)         
    floor = models.CharField(blank=True, null=True, max_length = 3)       
    floors = models.CharField(blank=True, null=True, max_length = 3)      
    m2 = models.CharField(blank=True, null=True, max_length = 10)          
    addr = models.TextField(blank=True, null=True, max_length = 80)        
    price = models.IntegerField(blank=True, null=True)    
    date = models.DateTimeField(blank=True, null=True)    
    last_updated = models.CharField(blank=True, null=True, max_length = 20)
    linkimg = models.CharField(blank=True, null=True, max_length = 200)     
    descr = models.TextField(blank=True, null=True)       
    tel = models.CharField(blank=True, null=True, max_length = 12)         
    region = models.TextField(blank=True, null=True)      
    agent = models.IntegerField(blank=True, null=True)    
                                                          
    class Meta:                                           
        managed = False                                   
        db_table = 'flat'
