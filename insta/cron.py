def delete_expired_stories():
    """
    Function to delete expired stories every day
    """
    print(Story.objects.filter(created_at__lt=(datetime.datetime.now()-datetime.timedelta(days=1))).delete())
