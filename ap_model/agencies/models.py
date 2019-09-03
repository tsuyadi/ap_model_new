from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django_extensions.db.models import TimeStampedModel
from mptt.models import MPTTModel, TreeForeignKey
from ap_model.ap_models_utils.functions import upload_path, form_upload_path, image_path


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


class AshAdmin(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ash_code = models.CharField(max_length=255, blank=True)
    ash_username = models.CharField(max_length=255, blank=True)

    class Meta:
        app_label = 'agencies'
        verbose_name = u"Ash Admin"
        verbose_name_plural = u"Ash Admins"

    def __init__(self, *args, **kwargs):
        super(AshAdmin, self).__init__(*args, **kwargs)

    def __unicode__(self):
        return "Admin for Ash %s" % self.ash_code


class Phone(TimeStampedModel):
    """Table for Agent Phone Numbers"""
    FIXLINE = 1
    MOBILE = 2
    TYPES = (
        (FIXLINE, 'Fix Line'),
        (MOBILE, 'Mobile')
    )

    agent_profile = models.ForeignKey(AgentProfile, blank=True, null=True, on_delete=models.CASCADE)
    type = models.PositiveSmallIntegerField(choices=TYPES, blank=True,
                                            null=True)
    number = models.CharField(max_length=255, default="", blank=True)
    is_active = models.BooleanField(default=False)
    is_default = models.BooleanField(default=True)

    class Meta:
        app_label = 'agencies'
        verbose_name = u"Phone"
        verbose_name_plural = u"Agent Phones"

    def __init__(self, *args, **kwargs):
        super(Phone, self).__init__(*args, **kwargs)

    def __unicode__(self):
        return "Phone for %s" % self.agent_profile.user.username


class Address(TimeStampedModel):
    """Table for Agent Address"""
    agent_profile = models.ForeignKey(AgentProfile, blank=True, null=True, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    is_default = models.BooleanField(default=True)
    address = models.TextField(default="", blank=True)
    zipcode = models.CharField(max_length=6, default="", blank=True)

    class Meta:
        app_label = 'agencies'
        verbose_name = u"Address"
        verbose_name_plural = u"Agent Address"

    def __init__(self, *args, **kwargs):
        super(Address, self).__init__(*args, **kwargs)

    def __unicode__(self):
        return "Address for %s" % self.agent_profile.user.username


class Bank(TimeStampedModel):
    """Table for Agent Bank Account"""
    agent_profile = models.ForeignKey(AgentProfile, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default="", blank=True)
    account_no = models.CharField(max_length=255, default="", blank=True)
    account_holder_name = models.CharField(max_length=255, default="",
                                           blank=True)
    is_default = models.BooleanField(default=True)

    class Meta:
        app_label = 'agencies'
        verbose_name = u"Bank"
        verbose_name_plural = u"Agent Bank Account"

    def __init__(self, *args, **kwargs):
        super(Bank, self).__init__(*args, **kwargs)

    def __unicode__(self):
        return "Bank Account for %s" % self.agent_profile.user.username


class Manpower(TimeStampedModel):
    agent = models.ForeignKey(AgentProfile, on_delete=models.CASCADE)
    ra = models.IntegerField(default=0)
    aa = models.IntegerField(default=0)
    nr = models.IntegerField(default=0)
    at = models.IntegerField(default=0)
    reactive_agent = models.IntegerField(default=0)  # updated 22022017
    case_group = models.IntegerField(default=0, blank=False)
    case_personal = models.IntegerField(default=0, blank=False)
    qc_personal = models.DecimalField(null=True, blank=True, max_digits=15, decimal_places=2)
    qc_group = models.DecimalField(null=True, blank=True, max_digits=15, decimal_places=2)
    position = models.CharField(max_length=2)
    hierdate = models.DateField(blank=False)

    class Meta:
        app_label = 'agencies'
        verbose_name = 'manpower'
        verbose_name_plural = "Agent Manpower"

    def __init__(self, *args, **kwargs):
        super(Manpower, self).__init__(*args, **kwargs)

    def __unicode__(self):
        return "Manpower for %s - %s" % (self.agent.code, self.hierdate)

    def save(self, *args, **kwargs):
        super(Manpower, self).save(*args, **kwargs)


@receiver(post_save, sender=Phone)
@receiver(post_save, sender=Address)
@receiver(post_save, sender=Phone)
def model_with_default_post_save(sender, **kwargs):
    """
    post save signal to invalidate any is_default flag if
    just saved object is the new default
    """
    instance = kwargs.get("instance")
    if instance.is_default:
        sender.objects.filter(
            agent_profile=instance.agent_profile, is_default=True
        ).exclude(pk=instance.id).update(
            is_default=False
        )


class DepartmentCategory(TimeStampedModel):
    name = models.CharField(max_length=255, blank=True)

    class Meta:
        app_label = 'agencies'
        verbose_name = u"DepartmentCategory"
        verbose_name_plural = u"DepartmentCategories"

    def __unicode__(self):
        return "DepartmentCategory for %s" % self.name


class Department(TimeStampedModel):
    department_category = models.ForeignKey(DepartmentCategory, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)

    class Meta:
        app_label = 'agencies'
        verbose_name = u"Department"
        verbose_name_plural = u"Departments"

    def __unicode__(self):
        return "Department for %s" % self.name


class UserDepartment(TimeStampedModel):
    code = models.PositiveIntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    class Meta:
        app_label = 'agencies'
        verbose_name = u"User Department"
        verbose_name_plural = u"User Departments"

    def __unicode__(self):
        return "User Department for %s" % self.name


class UserRole(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.ForeignKey(UserDepartment, on_delete=models.CASCADE)
    rd_code = models.ForeignKey(User, blank=True, null=True, default="", related_name="pa_relation_rd_code", on_delete=models.CASCADE)

    class Meta:
        app_label = 'agencies'
        verbose_name = u"User Role"
        verbose_name_plural = u"User Roles"

    def __unicode__(self):
        return "User Role for %s" % self.user.username


class ManpowerSummary(TimeStampedModel):
    agent_code = models.CharField(max_length=10, default=None, null=True)
    tipe = models.CharField(max_length=5)
    new_recruit_personal = models.IntegerField(default=0)
    new_recruit_group = models.IntegerField(default=0)
    terminated = models.IntegerField(default=0)
    reactive_agent = models.IntegerField(default=0)  # updated 22022017
    transfer_agent_in = models.IntegerField(default=0) # updated 27032017
    transfer_agent_out = models.IntegerField(default=0) # updated 27032017
    demotion_agent = models.IntegerField(default=0)
    promotion_agent = models.IntegerField(default=0)
    end_mp = models.IntegerField(default=0)
    total_man = models.IntegerField(default=0)
    vc = models.DecimalField(default=0, max_digits=15, decimal_places=2) #validated case
    vaa = models.IntegerField(default=0) # validated active agent
    #ar = models.DecimalField(default=0, max_digits=15, decimal_places=2)
    activity_ratio = models.DecimalField(default=0, max_digits=15, decimal_places=2)
    mapr = models.DecimalField(default=0, max_digits=15, decimal_places=2)
    maapr = models.DecimalField(default=0, max_digits=15, decimal_places=2)
    maspr = models.DecimalField(default=0, max_digits=15, decimal_places=2)
    maaspr = models.DecimalField(default=0, max_digits=15, decimal_places=2)

    def __init__(self, *args, **kwargs):
        super(ManpowerSummary, self).__init__(*args, **kwargs)

    def __unicode__(self):
        return "Manpower Summary for %s %s" % (self.agent_code, self.tipe)


class ManpowerSummaryNew(TimeStampedModel):
    agent_code = models.CharField(max_length=10, default=None, null=True)
    tipe = models.CharField(max_length=5)
    new_recruit_active = models.IntegerField(default=0)
    new_recruit_personal = models.IntegerField(default=0)
    new_recruit_group = models.IntegerField(default=0)
    terminated = models.IntegerField(default=0)
    #reactive_agent = models.IntegerField(default=0)  # updated 22022017
    #transfer_agent_in = models.IntegerField(default=0) # updated 27032017
    #transfer_agent_out = models.IntegerField(default=0) # updated 27032017
    demotion_agent = models.IntegerField(default=0)
    promotion_agent = models.IntegerField(default=0)
    end_mp = models.IntegerField(default=0)
    total_man = models.IntegerField(default=0)
    vc = models.DecimalField(default=0, max_digits=15, decimal_places=2) #validated case
    vaa = models.IntegerField(default=0) # validated active agent
    #ar = models.DecimalField(default=0, max_digits=15, decimal_places=2)
    activity_ratio = models.DecimalField(default=0, max_digits=15, decimal_places=2)
    mapr = models.DecimalField(default=0, max_digits=15, decimal_places=2)
    maapr = models.DecimalField(default=0, max_digits=15, decimal_places=2)
    maspr = models.DecimalField(default=0, max_digits=15, decimal_places=2)
    maaspr = models.DecimalField(default=0, max_digits=15, decimal_places=2)

    def __init__(self, *args, **kwargs):
        super(ManpowerSummaryNew, self).__init__(*args, **kwargs)

    def __unicode__(self):
        return "Manpower Summary for %s %s" % (self.agent_code, self.tipe)


class AgentNewRecruit(TimeStampedModel):
    leader_agent = models.ForeignKey(AgentProfile, null=True, blank=True, on_delete=models.CASCADE)
    recruited_code = models.ForeignKey(AgentProfile, null= True, blank=True, related_name='recruits', on_delete=models.CASCADE)
    recruited_license_date = models.DateField(null=True, blank=True)
    recruited_level = models.CharField(max_length=255, null=True, blank=True)
    recruiter_code = models.ForeignKey(AgentProfile, null=True, blank=True, related_name='recruiters', on_delete=models.CASCADE)

    class Meta:
        app_label = 'agencies'
        verbose_name = u"Agent New Recruit"
        verbose_name_plural = u"Agent New Recruits"

    def __init__(self, *args, **kwargs):
        super(AgentNewRecruit, self).__init__(*args, **kwargs)

    def __unicode__(self):
        return "New recruit for %s" % (self.leader_agent)


class AgentDashboard(TimeStampedModel):
    agent = models.ForeignKey(AgentProfile, related_name="agent_dashboard", on_delete=models.CASCADE)
    group = models.IntegerField()
    ape_wtd = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    ape_mtd = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    ape_ytd = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    fyp_wtd = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    fyp_mtd = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    fyp_ytd = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    fyc_nb_wtd = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    fyc_wtd = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    fyc_mtd = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    fyc_ytd = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    fyc_rw = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    syc_wtd = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    syc_mtd = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    syc_ytd = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    afyp_wtd = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    afyp_mtd = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    afyp_ytd = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    afyc_wtd = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    afyc_mtd = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    afyc_ytd = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    qc_wtd = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    qc_mtd = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    qc_ytd = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    qc_rw = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    weeklybonus_wtd = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    weeklybonus_mtd = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    weeklybonus_ytd = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    direct_dm = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    direct_sm = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    direct_fc = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    fyc_mtd_paralel = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    syc_mtd_paralel = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    mio_paralel = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    mio_group = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    mio_total = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    mpa = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    mib = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    income_total = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    nr_mtd_fc = models.IntegerField(default=0)
    nr_mtd_sm = models.IntegerField(default=0)
    nr_mtd_dm = models.IntegerField(default=0)
    nr_mtd_rm = models.IntegerField(default=0)
    nr_mtd_rd = models.IntegerField(default=0)
    nr_ytd_fc = models.IntegerField(default=0)
    nr_ytd_sm = models.IntegerField(default=0)
    nr_ytd_dm = models.IntegerField(default=0)
    nr_ytd_rm = models.IntegerField(default=0)
    nr_ytd_rd = models.IntegerField(default=0)
    fc_to_leader_ratio = models.DecimalField(max_digits=25, decimal_places=2, default=0)

    class Meta:
        app_label = 'agencies'
        verbose_name = u"Agent Dashboard"
        verbose_name_plural = u"Agent Dashboard"

    def __init__(self, *args, **kwargs):
        super(AgentDashboard, self).__init__(*args, **kwargs)

    def __unicode__(self):
        return "Dashboard for %s" % (self.agent.code)


class TakumiDashboard(TimeStampedModel):
    agent = models.ForeignKey(AgentProfile, related_name="takumi_dashboard", on_delete=models.CASCADE)
    group = models.IntegerField(default=0)
    ape_wtd = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    ape_mtd = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    ape_ytd = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    ap_wtd = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    ap_mtd = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    ap_ytd = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    aap_wtd = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    aap_mtd = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    aap_ytd = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    ec_submit_wtd = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    ec_submit_mtd = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    ec_submit_ytd = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    ec_submit_rw = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    ec_issued_wtd = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    ec_issued_mtd = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    ec_issued_ytd = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    ec_issued_rw = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    fyc_wtd = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    fyc_mtd = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    fyc_ytd = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    syc_wtd = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    syc_mtd = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    syc_ytd = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    cap_wtd = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    cap_mtd = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    cap_ytd = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    monthly_bonus = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    yearly_bonus = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    license = models.BooleanField(default=0)
    training = models.BooleanField(default=0)
    probation = models.BooleanField(default=0)
    extend_probation = models.BooleanField(default=0)
    effective_days = models.IntegerField(default=0)
    effective = models.BooleanField(default=0)
    effective_ratio = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    monthly_allowance_wtd = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    monthly_allowance_mtd = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    acc_monthly_allowance = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    acc_extra_allowance = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    acc_monthly_allowance_deficit = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    extra_allowance = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    overriding_personal_selling_year1 = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    overriding_personal_selling_year2 = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    overriding_group_selling_year1 = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    overriding_group_selling_year2 = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    overriding = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    percentage_monthly_bonus = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    acc_tc_monthly_bonus = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    acc_tm_monthly_bonus = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    acc_td_monthly_bonus = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    percentage_yearly_bonus = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    acc_tc_yearly_bonus = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    acc_tm_yearly_bonus = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    acc_td_yearly_bonus = models.DecimalField(max_digits=25, decimal_places=2, default=0)

    class Meta:
        app_label = 'agencies'
        verbose_name = u"Takumi Dashboard"
        verbose_name_plural = u"Takumi Dashboard"

    def __init__(self, *args, **kwargs):
        super(TakumiDashboard, self).__init__(*args, **kwargs)

    def __unicode__(self):
        return "Dashboard for %s" % (self.agent.code)


class AgentLevelAsh(TimeStampedModel):
    agent_code = models.CharField(max_length=25, blank=True, null=True, verbose_name='Agent Code')
    position = models.CharField(max_length=25, blank=True, null=True, verbose_name='Position')
    amb_code = models.CharField(max_length=25, blank=True, null=True, verbose_name='Agency Manager Builder')
    rmb_code = models.CharField(max_length=25, blank=True, null=True, verbose_name='Regional Management Builder')
    rd_code = models.CharField(max_length=25, blank=True, null=True, verbose_name='Regional Director')
    ash_code = models.CharField(max_length=25, blank=True, null=True, verbose_name='Agency Sales Head')
    hierarchy_date = models.DateField(max_length=25, blank=True, null=True, verbose_name='Hierarchy Date')

    class Meta:
        app_label = 'agencies'
        verbose_name = u"Agent Level For Ash"
        verbose_name_plural = u"Agent Level Ashs"

    def __init__(self, *args, **kwargs):
        super(AgentLevelAsh, self).__init__(*args, **kwargs)

    def __unicode__(self):
        return "Agent Level for %s" % (self.agent_code)


# TODO : calculate how many times agent log in to AP
class UserLogin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()


class AccountLockoutNew(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lock_count = models.IntegerField(default=0)
    is_locked = models.BooleanField(default=False)
    lock_until = models.DateTimeField(null=True, blank=True)


class Notifications(models.Model):
    ALL='A'
    AGENT='D'
    GROUP='G'
    TARGETS=(
        (ALL, "All"),
        (AGENT, "Agent"),
        (GROUP,  "Group"))

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    target = models.CharField(max_length=1, choices=TARGETS, default=ALL)
    start = models.DateField()
    end = models.DateField()
    title = models.TextField()
    priority = models.IntegerField(default=0)
    content = models.TextField(blank=True, null=True)


# def user_presave(sender, instance, **kwargs):
#     if instance.last_login:
#         old = instance.__class__.objects.get(pk=instance.pk)
#         if instance.last_login != old.last_login:
#             instance.userlogin_set.create(timestamp=instance.last_login)
#
# pre_save.connect(user_presave, sender=User)


class LoggedInUser(models.Model):
    user = models.OneToOneField(User, related_name='logged_in_user', on_delete=models.CASCADE)
    # Session keys are 32 characters long
    session_key = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return self.user.username


class UserLoginActivity(models.Model):
    # Login Status
    SUCCESS = 'S'
    FAILED = 'F'

    LOGIN_STATUS = ((SUCCESS, 'Success'),
                           (FAILED, 'Failed'))

    login_IP = models.GenericIPAddressField(null=True, blank=True)
    login_datetime = models.DateTimeField(auto_now=True)
    login_username = models.CharField(max_length=40, null=True, blank=True)
    status = models.CharField(max_length=1, default=SUCCESS, choices=LOGIN_STATUS, null=True, blank=True)
    user_agent_info = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'user_login_activity'
        verbose_name_plural = 'user_login_activities'


class MobileUser(TimeStampedModel):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    platform = models.CharField(max_length=255, blank=True, null=True)
    deviceName = models.CharField(max_length=255, blank=True, null=True)
    osVersion = models.CharField(max_length=255, blank=True, null=True)
    loginTime = models.CharField(max_length=255, blank=True, null=True)
    imei = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'Mobile User'
        verbose_name_plural = 'Mobile Users'

    def __unicode__(self):
        return "User login from %s" % self.deviceName


class DashBoardImageSlider(TimeStampedModel):
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    image = models.ImageField(blank=True, upload_to=image_path)
    description = models.TextField(blank=True)
    published = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Dashboard Image Slider'
        verbose_name_plural = 'Dashboard Image Slider'

    def __unicode__(self):
        return "Create by [%s] on %s" % (self.owner, self.created)


class FileUpload(TimeStampedModel):
    """Table for Memo """
    MEMO=1
    FORM=2
    TRAINING=3
    HOSPITALPROVIDER=4
    MEDICALTABLE=5
    SALESILUSTRATION=6
    GUIDANCE=7
    GUIDEAMS = 8
    FUNDFACTSHEET = 9
    GUIDETMC = 10
    TYPES=(
        (MEMO, "Memo"),
        (FORM, "Form"),
        (TRAINING, "Training"),
        (HOSPITALPROVIDER, "HospitalProvider"),
        (MEDICALTABLE, "MedicalTable"),
        (SALESILUSTRATION, "SalesIlustration"),
        (GUIDANCE, "Guidance"),
        (GUIDEAMS, "GuideAms"),
        (FUNDFACTSHEET, "FundFactSheet"),
        (GUIDETMC, "GuideTmc")
        )
    ALL = 1
    AGENCY = 2
    TAKUMI = 3
    BANCA = 4
    TARGETS =(
        (ALL, "All"),
        (AGENCY, "Agency"),
        (TAKUMI, "Takumi"),
        (BANCA, "Banca"),
        )
    department_category = models.ForeignKey(DepartmentCategory, null=True, blank=True, on_delete=models.CASCADE)  # update 21122016
    department = models.ForeignKey(Department, null=True, blank=True, on_delete=models.CASCADE)
    type = models.PositiveSmallIntegerField(choices=TYPES, blank=False, null=False)
    target = models.PositiveSmallIntegerField(choices=TARGETS, default=1, null=False)
    name = models.CharField(max_length=255)
    effective_date_start = models.DateField(blank=True, null=True)
    effective_date_end = models.DateField(blank=True, null=True)
    filename = models.FileField(upload_to=form_upload_path)

    class Meta:
        app_label = 'agencies'
        verbose_name = u"FileUpload"
        verbose_name_plural = u"FileUploads"

    def __init__(self, *args, **kwargs):
        super(FileUpload, self).__init__(*args, **kwargs)

    def __unicode__(self):
        return "FileUpload for %s" % self.name

