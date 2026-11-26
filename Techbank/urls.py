from django.urls import path
from.import views
urlpatterns=[
    path('',views.home),
    path('home',views.home),

    path('Reg',views.Reg),
    path('Register',views.Register),
    

    path('userlogin',views.userlogin),
    path('userlog',views.userlog),
    path('showuserpage',views.showuserpage),
    path('showuserreg',views.showuserreg),
    path('logout_user',views.logout_user, name='logout1'),

    path('adminregpage',views.adminregpage),
    path('adminreg',views.adminreg),
    path('showadminreg',views.showadminreg),
    path('logout_admin',views.logout_admin, name='logout2'),

    path('adminlogin',views.adminlogin),
    path('adminlog',views.adminlog),
    path('showadminpage',views.showadminpage),    

    
    path('complaint',views.complaint),
    path('transaction',views.transaction),
    path('transaction2',views.transaction2),
    path('transfer',views.transfer),
    path('showtrans',views.showtrans),
    
   path('edit/<int:id>',views.edit),
   path('edcode/<int:id>',views.edcode),
   path('contact_us',views.contact_us),

   
   path('usercomplaint',views.usercomplaint),
   path('complnt',views.complnt),
   path('showcomplaint',views.showcomplaint),

   path('admin_dele/<int:id>',views.admin_dele),
   path('trans_dele/<int:id>',views.trans_dele),
   path('user_dele/<int:id>',views.user_dele),
   
   path('customer_details',views.customer_details),

   path('search_customer', views.search_customer),
   path('balance_quary',views.balance_quary),

]