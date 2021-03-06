from rest_framework.permissions import BasePermission
from oscarapi.basket.operations import request_contains_basket, request_contains_line


class HasUser(BasePermission):
    "Only anonymous and authenticated users can access this resource."
    def has_permission(self, request, view):
        return request.user


class IsAdminUserOrRequestContainsBasket(HasUser):
    """
    Permission class that checks if a request contains a basket.
    """

    def has_object_permission(self, request, view, obj):
        return request_contains_basket(request, obj) or request.user.is_staff


class IsAdminUserOrRequestContainsLine(BasePermission):
    """
    Permission class that checks if a request contains the basket this line
    belongs to.
    """
    def has_object_permission(self, request, view, obj):
        return request_contains_line(request, obj) or request.user.is_staff


class IsAdminUserOrRequestContainsWishList(HasUser):
    """
    Permission class that checks if a request contains a basket.
    """

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user or request.user.is_staff


class IsAdminUserOrRequestContainsWishListLine(BasePermission):
    """
    Permission class that checks if a request contains the basket this line
    belongs to.
    """
    def has_object_permission(self, request, view, obj):
        return obj.wishlist.owner == request.user or request.user.is_staff
