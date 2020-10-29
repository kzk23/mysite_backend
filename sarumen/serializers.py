from rest_framework.serializers import ModelSerializer, IntegerField
from rest_framework.serializers import CurrentUserDefault, HiddenField
from sarumen.models import Post, Category, Tag

class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug',)


class TagSerializer(ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'name', 'slug',)


class PostSerializer(ModelSerializer):
    author = HiddenField(default=CurrentUserDefault())
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(read_only=True)

    class Meta:
        model = Post
        field = ["id", "author", "category", "tags", "thumnail", "titile", "text", "created_at"],