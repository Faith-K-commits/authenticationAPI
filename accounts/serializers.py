from .models import Organisation, User
from rest_framework import serializers


class OrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = ['orgId', 'name', 'description']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['userId', 'firstName', 'lastName', 'email', 'phone', 'password']
        extra_kwargs = {'password': {'write_only': True}}  # Disable password retrieval

    # Handle creation of a new user
    def create(self, validated_data):
        user = User(
            firstName=validated_data['firstName'],
            lastName=validated_data['lastName'],
            email=validated_data['email'],
            phone=validated_data['phone'],
        )
        user.set_password(validated_data['password'])
        user.save()

        # Create an associated organisation
        orgName = f"{validated_data['firstName']}'s Organisation"
        organisation = Organisation.objects.create(name=orgName, description="Default Organization")
        user.organisations.add(organisation)

        return user

    def validate(self, data):
        errors = []
        for field, value in data.items():
            try:
                self.fields[field].run_validators(value)

            except serializers.ValidationError as e:
                errors.append({'field': field, 'message': str(e)})
        if errors:
            raise serializers.ValidationError({"errors": errors})
        return data
