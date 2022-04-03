from rest_framework import serializers
from ..models import User

class registerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "mobile_no", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def save(self):
        """
        Overriding the save method of the user model where we can validate the fields and check if both
        passwords typed by the user is the same
        """
        user = User(
            email=self.validated_data["email"],
            username=self.validated_data["username"],
            mobile_no=self.validated_data["mobile_no"],
        )
        try:
            if User.objects.get(email=self.validated_data["email"]):
                raise serializers.ValidationError(
                    {
                        "email": "Email with user already exists"
                    }
                )
        except User.DoesNotExist:
            password = self.validated_data["password"]
            user.set_password(password)
            user.save()

            return user
