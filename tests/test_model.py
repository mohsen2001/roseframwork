import pytest

from data.models import TestMyModel


#
# @pytest.fixture(scope='session', autouse=True)
# def configure_test_settings():
#     settings.configure(
#         INSTALLED_APPS=['tests'],
#         DATABASES={
#             'default': {
#                 'ENGINE': 'django.db.backends.sqlite3',
#                 'NAME': ':memory:'
#             }
#         },
#     )
#     django.setup()



@pytest.mark.django_db
def test_create():
    instance = TestMyModel.objects.create(field1="example", field2='00123', user_created=1, ip_created='192.168.59.2')
    assert instance.field1 == "example"
    assert instance.field2 == "00123"
    assert instance.ip_created == "192.168.59.2"
    assert instance.user_created == 1
    assert instance.date_created is not None
    assert instance.record_uuid is not None


@pytest.mark.django_db
def test_update():
    instance = TestMyModel.objects.create(field1="example update", field2='00123', user_created=1,
                                          ip_created='192.168.59.4')
    item_record_uuid = instance.record_uuid
    instance.ip_updated = '192.168.1.10'
    instance.user_updated = 2
    instance.save()
    assert instance.field1 == "example update"
    assert instance.field2 == "00123"
    assert instance.ip_created == "192.168.59.4"
    assert instance.user_created == 1
    assert instance.date_created is not None
    assert instance.ip_updated == '192.168.1.10'
    assert instance.user_updated == 2
    assert instance.date_updated is not None
    assert instance.record_uuid == item_record_uuid
