from flask import Blueprint
from .admin_views import Foods, SpecificOrder, SpecificFoodItem, AcceptFoodOrders, AcceptedOrders, RejectFoodOrders, CompletedOrders, CompleteFoodOrders, GetOrders, OrderHistoryForSpecificUser


admin_blueprint = Blueprint("admin", __name__)
