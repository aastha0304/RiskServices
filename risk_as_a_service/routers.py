from rest_framework import routers
from risk_apis.views import RiskViewSet

router = routers.SimpleRouter()
router.register(r'risk', RiskViewSet) #, base_name='risk')