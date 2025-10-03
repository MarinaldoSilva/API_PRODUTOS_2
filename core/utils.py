from rest_framework import status
from typing import Union
from .service import MSG_PRODUTO_NAO_LOCALIZADO 


def get_status_errors(errors:Union[dict, list]) -> int:
    if isinstance(errors, dict) and 'error' in errors:
        """
        isinstance tem a função de verificar o tipo, por exemplo:
            pergunta errors é do tipo dicionário? e o and pergunta se Errors esta presente nesse dict
            o fluxo segue e podemos fazer as validações normalmente
        """
        if errors['error'] == MSG_PRODUTO_NAO_LOCALIZADO :
            return status.HTTP_404_NOT_FOUND #erros de não localizado
    return status.HTTP_400_BAD_REQUEST #errors de validação