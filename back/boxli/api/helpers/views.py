class CustomSerializers(object):
    def get_serializer_class(self):
        """Allows multiple serializers per view depending on incoming request"""
        serializers = {
            'GET': 'list_serializer',
            'POST': 'create_serializer',
            'PUT': 'retrieve_serializer',
            'PATCH': 'retrieve_serializer'
        }
        request_method = self.request.method.upper()

        if request_method in serializers:
            serializer_class = getattr(self, serializers[request_method])
        else:
            serializer_class = super(CustomSerializers, self).get_serializer_class()
        return serializer_class
