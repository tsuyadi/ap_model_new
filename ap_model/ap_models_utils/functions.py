# coding: utf-8

# python libs
import os
# django libs
from django.utils import timezone


def upload_path(instance, name):
    """Provide a dynamic path for uploading file"""
    now = timezone.now()
    return os.path.join(now.strftime("%Y"), now.strftime("%m"), now.strftime("%d")
    ) + name


def form_upload_path(instance, name):
    """Provide a dynamic path for uploading file"""
    now = timezone.now()
    return os.path.join(instance.get_type_display() + '/' +
        now.strftime("%Y"), now.strftime("%m"), now.strftime("%d")
    ) + name


def certificate_upload_path(instance, name):
    """Provide a dynamic path for uploading file"""
    now = timezone.now()
    return os.path.join('CERTIFICATE' + '/' + instance.certificate + '/' +
        now.strftime("%Y"), now.strftime("%m"), now.strftime("%d")
    ) + name


def spaj_support_document_path(instance, name):
    now = timezone.now()
    return os.path.join('SPAJ' + '/' + instance.spaj.number + '/' +
                        now.strftime("%Y"), now.strftime("%m"), now.strftime("%d")
                        ) + name


def policy_support_document_path(instance, name):
    now = timezone.now()
    return os.path.join('POLICY' + '/' + instance.policy.number + '/' +
                        now.strftime("%Y"), now.strftime("%m"), now.strftime("%d")
                        ) + name


def investment_transaction_report_path(instance, name):
    now = timezone.now()
    return os.path.join(instance + '/' +
                        now.strftime("%Y"), now.strftime("%m"), now.strftime("%d")
                        ) + name


def annual_investment_transaction_report_path(instance, name):
    now = timezone.now()
    return os.path.join(instance + '/' +
                        now.strftime("%Y"), now.strftime("%m"), now.strftime("%d")
                        ) + name


def reporting_path(instance, name):
    return os.path.join('Reporting' + '/' + instance.get_type_display() + '/' + str(instance.agent.code) + '/' + str(instance.year)) + '/' + name


def image_path(instance, name):
    return os.path.join('Image' + '/' + instance.image.name)
