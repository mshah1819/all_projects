from django.conf.urls import patterns, url

from mooc import views

urlpatterns = patterns('',
#    top related views
    url(r'^$', views.index, name='index'),
    url(r'^signup/$', views.signup), #Only Takes care of Loading the Sign Up HTML Page.
    url(r'^add_user/$', views.add_user), # Handles User Sign Up Form.
    url(r'^login/$', views.login_user, name='signin'),
    url(r'^home/$', views.home),

#    user related views
    url(r'^profile/$', views.profile),
    url(r'^update_user/$', views.update_user),
    url(r'^logout/$', views.logout_user),

#    category related views
    url(r'^list_category/$', views.list_category),
    url(r'^category/$', views.category),
    url(r'^add_category/$', views.add_category),
    url(r'^remove_category/$', views.remove_category),

#    course related views
    url(r'^list_course/$', views.list_course),
    url(r'^course/$', views.course),
    url(r'^add_course/$', views.add_course),
    url(r'^remove_course/$', views.remove_course),
    url(r'^get_course/$', views.get_course),

#   course and user related activity    
    url(r'^enroll_course/$', views.enroll_course),
    url(r'^drop_course/$', views.drop_course),

#    announcement related activity
    url(r'^list_announcement/$', views.list_announcement),    
    url(r'^announcement/$', views.announcement),
    url(r'^add_announcement/$', views.add_announcement),
    url(r'^edit_announcement/$', views.edit_announcement),
    url(r'^update_announcement/$', views.update_announcement),
    url(r'^remove_announcement/$', views.remove_announcement),
    url(r'^get_announcement/$', views.get_announcement),
    
#    discussion related activity
    url(r'^discussion/$', views.discussion),
    url(r'^add_discussion/$', views.add_discussion),
    url(r'^get_discussion/$', views.get_discussion),
    url(r'^edit_discussion/$', views.edit_discussion),
    url(r'^list_discussion/$', views.list_discussion),
    url(r'^update_discussion/$', views.update_discussion),
    url(r'^remove_discussion/$', views.remove_discussion),
    url(r'^message/$', views.message),
    url(r'^add_message/$', views.add_message),
    url(r'^remove_message/$', views.remove_message),
    url(r'^edit_message/$', views.edit_message),
    url(r'^update_message/$', views.update_message),
#    quiz related activity
    url(r'^quiz/$', views.quiz),
    url(r'^add_quiz/$', views.add_quiz),
    url(r'^add_questionhtml/$', views.show_addquestionhtml),
    url(r'^add_question/$', views.add_question),
    url(r'^list_quiz/$', views.list_quiz),
    url(r'^update_quiz/$', views.update_quiz),
    url(r'^get_quiz/$', views.get_quiz),
    url(r'^remove_quiz/$', views.remove_quiz),
    url(r'^edit_quiz/$', views.edit_quiz),
    url(r'^evaluate_quiz/$', views.evaluate_quiz),
)
