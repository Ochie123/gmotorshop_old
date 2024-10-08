from io import BytesIO
import logging
import PIL
from PIL import Image
from django.core.files.base import ContentFile 
from django.db.models.signals import pre_save 
from django.dispatch import receiver
from .models import ProductImage 
#hh
from django.contrib.auth.signals import user_logged_in 

###tokennn
from django.conf import settings


from django.db.models.signals import pre_save, post_save 
from .models import ProductImage

THUMBNAIL_SIZE = (50, 50)
logger = logging.getLogger(__name__)

@receiver(pre_save, sender=ProductImage)
def generate_thumbnail(sender, instance, **kwargs):
    logger.info(
        "Generating thumbnail for product %d", 
        instance.product.uuid,
)
    image = Image.open(instance.image)
    image = image.convert("RGB") 
    image.thumbnail(THUMBNAIL_SIZE, PIL.Image.Resampling.LANCZOS)
    temp_thumb = BytesIO() 
    image.save(temp_thumb, "JPEG") 
    temp_thumb.seek(0)
    # set save=False, otherwise it will run in an infinite loop
    instance.thumbnail.save( 
        instance.image.name, 
        ContentFile(temp_thumb.read()), 
        save=False,
)   
    temp_thumb.close()
