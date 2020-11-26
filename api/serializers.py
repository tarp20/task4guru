from rest_framework import serializers
from .models import Car, Rating
from .utils import is_car_exist


class CarSerializers(serializers.ModelSerializer):

    average_rank = serializers.DecimalField(
        decimal_places=1, max_digits=10, read_only=True)
    car_id = serializers.IntegerField(source='id', read_only=True)

    class Meta:
        model = Car
        fields = ['car_id', 'Make_Name', 'Model_Name', 'average_rank']

    def create(self, validated_data):
        Make_Name = validated_data['Make_Name']
        Model_Name = validated_data['Model_Name']
        if is_car_exist(Make_Name, Model_Name):
            try:
                Car.objects.get(Make_Name=Make_Name, Model_Name=Model_Name)
                message = {
                'Error': 'This car already exists in our database'}
                raise serializers.ValidationError(message)
            except Car.DoesNotExist:
                return Car.objects.create(Make_Name=Make_Name,
                                          Model_Name=Model_Name)
        else:
            message = {
                'Error': 'This car does not exist ,\
                 provide car make and model correctly'}
            raise serializers.ValidationError(message)


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ['car_id', 'rating']


class CarsPopularSerializer(serializers.ModelSerializer):
    total_ratings = serializers.IntegerField(read_only=True)

    class Meta:
        model = Car
        fields = ['Make_Name', 'Model_Name', 'total_ratings']
