from django.db import models

# Create your models here.
from django.db import models
from join.models import *
from inventory.models import *

class UserCart(models.Model):
    '''외래키 사용 방법'
    models.ForeignKey(참조할 테이블, related_name = 개체 관계에서 사용할 이름, on_delete = 개체 삭제시 수행할 동작, db_column= 매개변수를 사용하지 않는다면, 데이터 베이스 필등서 작성될 필드명)
    참조할 테이블 => 외래키에서 어떤 테이블을 참조할 것인가
    개체 관계에서 사용할 이름 (related_name)
    개체 삭제시 수행할 동작
    models.CASCADE	외래키를 포함하는 행도 함께 삭제
    models.PROTECT	해당 요소가 함께 삭제되지 않도록 오류 발생 (ProtectedError)
    models.SET_NULL	외래키 값을 NULL 값으로 변경 (null=True일 때 사용 가능)
    models.SET(func)	외래키 값을 func 행동 수행 (func는 함수나 메서드 등을 의미)
    models.DO_NOTHING	아무 행동을 하지 않음
    '''
    user_id = models.ForeignKey(UserInfo, on_delete=models.DO_NOTHING)
    product_id = models.ForeignKey(Inventory, on_delete=models.DO_NOTHING)
    color = models.CharField(max_length=20)
    amount = models.IntegerField()
    purchase_date = models.DateField()
    price = models.IntegerField()








