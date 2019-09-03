from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.models import TimeStampedModel
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.
class Branch(TimeStampedModel):
    """Table for Branch"""
    name = models.CharField(max_length=255, default="", blank=True)
    address = models.TextField(default="", blank=True)
    phone = models.CharField(max_length=255, default="", blank=True)
    origin_id = models.CharField(max_length=255)
    office_code = models.CharField(max_length=255, default="", blank=True)

    class Meta:
        app_label = 'agencies'
        verbose_name = "Branch"
        verbose_name_plural = "Branch"

    def __init__(self, *args, **kwargs):
        super(Branch, self).__init__(*args, **kwargs)

    def __unicode__(self):
        return "Branch %s" % self.name


class UserBranch(TimeStampedModel):
    """Table for User Branch"""
    user = models.ForeignKey(User, default="", blank=True, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, default="", blank=True, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("user", "branch"),)
        app_label = 'agencies'
        verbose_name = "UserBranch"
        verbose_name_plural = "User Branchs"

    def __init__(self, *args, **kwargs):
        super(UserBranch, self).__init__(*args, **kwargs)

    def __unicode__(self):
        return "User %s to Branch %s" % (self.user.username,self.branch.name)

    def get_user(self):
        return self.User.username
    get_user.short_description = 'User'

    def get_branch(self):
        return self.branch.name
    get_branch.short_description = 'Branch'


class AgentProfile(TimeStampedModel):
    """Table for Agent Profile"""
    MALE = 1
    FEMALE = 2
    OTHER = 3
    GENDER_CHOICES = (
        (MALE, 'Pria'),
        (FEMALE, 'Wanita'),
        (OTHER, 'Other'),
    )

    MUSLIM = 1
    CHRISTIAN = 2
    CATHOLIC = 3
    HINDU = 4
    BUDDHIST = 5
    OTHER_RELIGION = 6
    RELIGION_CHOICES = (
        (MUSLIM, 'Islam'),
        (CHRISTIAN, 'Kristen'),
        (CATHOLIC, 'Katolik'),
        (HINDU, 'Hindu'),
        (BUDDHIST, 'Buddha'),
        (OTHER_RELIGION, 'Other Religion'),
    )

    SINGLE = 1
    MARRIED = 2
    DIVORCED = 3
    WIDOWED = 4
    OTHER_MARITAL_STATUS = 5
    MARITAL_STATUS = (
        (SINGLE, 'Belum Menikah'),
        (MARRIED, 'Menikah'),
        (DIVORCED, 'Cerai'),
        (WIDOWED, 'Duda/Janda'),
        (OTHER_MARITAL_STATUS, 'Other Marital Status')
    )

    ACTIVE = 1
    TERMINATE = 2
    RESIGN = 3
    OTHER_AGENT_STATUS = 4
    AGENT_STATUSES = (
        (ACTIVE, 'Active'),
        (TERMINATE, 'Terminate'),
        (RESIGN, 'Resign'),
        (OTHER_AGENT_STATUS, 'Other Agent Status'),
    )

    TK = 1
    K0 = 2
    K1 = 3
    K2 = 4
    K3 = 5
    OTHER_PTKP = 6
    PTKP_STATUSES = (
        (TK, 'Tidak Kawin'),
        (K0, 'Kawin Tidak Punya Anak'),
        (K1, 'Kawin Dengan Anak 1'),
        (K2, 'Kawin Dengan Anak 2'),
        (K3, 'Kawin Dengan Anak 3'),
        (OTHER_PTKP, 'Other PTKP'),
    )

    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, blank=True, null=True, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, default="",
                                 blank=True, null=True)
    code = models.CharField(max_length=255, default="", blank=True)
    status = models.PositiveSmallIntegerField(choices=AGENT_STATUSES,
                                              blank=True, null=True)
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES,
                                              blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    religion = models.PositiveSmallIntegerField(choices=RELIGION_CHOICES,
                                                blank=True, null=True)
    marital_status = models.PositiveSmallIntegerField(choices=MARITAL_STATUS,
                                                      blank=True, null=True)
    id_number = models.CharField(max_length=255, default="", blank=True)
    npwp_number = models.CharField(max_length=255, default="", blank=True,
                                   null=True)
    ptkp_status = models.PositiveSmallIntegerField(choices=PTKP_STATUSES,
                                                   blank=True, null=True)
    hire_date = models.DateField(blank=True, null=True, default=None)
    terminate_date = models.DateField(blank=True, null=True, default=None)
    aaji_number = models.CharField(max_length=255, default="", blank=True)
    aaji_license_date = models.DateField(blank=True, null=True, default=None)
    aaji_expired_date = models.DateField(blank=True, null=True, default=None)
    license_phase = models.CharField(max_length=255, default="", blank=True)
    contract_date = models.DateField(blank=True, null=True, default=None)
    fast_date = models.DateField(blank=True, null=True, default=None)
    origin_id = models.CharField(max_length=255, default="", blank=True)
    first_login = models.BooleanField(default=True)

    class Meta:
        app_label = 'agencies'
        verbose_name = "AgentProfile"
        verbose_name_plural = "Agent Profiles"

    def __init__(self, *args, **kwargs):
        super(AgentProfile, self).__init__(*args, **kwargs)

    def __unicode__(self):
        if self.user is not None:
            name = self.user.username
        else:
            name = self.code

        return "Agent Profile for %s" % name


class Level(MPTTModel, TimeStampedModel):
    """Table for Agent Level"""
    MANAGEMENT = 1
    BRANCH_ADMIN = 2
    BRANCH_MANAGEMENT = 102
    SRSH = 3
    RSH = 4
    RD = 5
    RMB = 6
    AMB = 7
    AMP = 14
    RMP = 8
    FC = 9
    SUB_MANAGEMENT = 10
    TD = 11
    TM = 12
    TC = 13
    ETC = 15
    STC = 16
    RBM = 17
    EBC = 18
    SBC = 19
    BC = 20

    LEVELS = (
        (MANAGEMENT, "Tokio Marine Management"),
        (SUB_MANAGEMENT, "Tokio Marine Sub Management"),  # update 23022017 (investment, underwriting, sales.support, and policyholder.services)
        (BRANCH_ADMIN, "Branch Admin"),
        (BRANCH_MANAGEMENT, "Branch Management"),  # update 20170911(branch_management)
        (SRSH, "Senior Regional Sales Head"),
        (RSH, "Regional Sales Head"),
        (RD, "Regional Director"),
        (RMB, "Regional Manager Builder"),
        (AMB, "Agency Manager Builder"),
        (AMP, "Agency Manager Producer"),
        (RMP, "Regional Manager Producer"),
        (FC, "Financial Consultant"),
        (TD, "Takumi Director"),  # updated for takumi scheme 20102017
        (TM, "Takumi Manager"),
        (TC, "Takumi Consultant"),
        (ETC, "Executive Takumi Consultant"),  # update for takumi scheme 28082018
        (STC, "Senior Takumi Consultant"),
        (RBM, "Regional Bancassurance Manager"),  # update for banca scheme 15082019
        (EBC, "Executive Bancassurance Consultant"),  # update for banca scheme 15082019
        (SBC, "Senior Bancassurance Consultant"),  # update for banca scheme 15082019
        (BC, "Bancassurance Consultant"),  # update for banca scheme 15082019
    )
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    type = models.PositiveSmallIntegerField(choices=LEVELS, blank=True,
                                            null=True)
    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name='children', db_index=True, on_delete=models.CASCADE)

    class MPTTMeta:
        """Meta class for MPTT based model"""
        order_insertion_by = ['user']

    class Meta:
        app_label = 'agencies'
        verbose_name = u"Level"
        verbose_name_plural = u"Agent Level"

    def __init__(self, *args, **kwargs):
        super(Level, self).__init__(*args, **kwargs)

    def __unicode__(self):
        return "Agent Level for %s" % self.user.username

