from slugify import slugify

#returns 32 cahracter long slug
def generateSlug(title):
    if len(title) > 32:
        title = title[:32]
    slug = slugify(title, allow_unicode=True)
    return slug