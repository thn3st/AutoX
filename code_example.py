import cloudinary
import cloudinary.uploader
import cloudinary.api
cloudinary.config(
    cloud_name="dwoxggxq7",
    api_key="585454961287396",
    api_secret="dTVgyVOuH2jsJNQ87aDn1DBQtTU"
)
# a = cloudinary.uploader.upload(["https://upload.wikimedia.org/wikipedia/commons/a/ae/Olympic_flag.jpg", "https://support.cloudinary.com/hc/article_attachments/5988822037522/media_library_upload_widget.jpg"],
#                                public_id="Olympic_flag.jpg")
#
# print(a)

result = cloudinary.api.resources()
print(result)
