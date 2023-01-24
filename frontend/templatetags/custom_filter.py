from django import template
from api.models import Branch, College, CutOFF,Exam,CutOFF,Branch
register = template.Library()

@register.filter()
def cutoff_filter_for_openingrank(branch_id,exam):
	try:
		branch=Branch.objects.get(id=branch_id)
		
		cutoff=CutOFF.objects.filter(branch=branch,gender="M",hs_or_al="AI",exam=exam).first()
		result=cutoff.cutoff_by_category.get("General").split("-")[0]
		
		return result
	except:
		return ""

@register.filter()
def cutoff_filter_for_closingrank(branch_id,exam):
	try:
		branch=Branch.objects.get(id=branch_id)
		cutoff=CutOFF.objects.filter(branch=branch,gender="M",hs_or_al="AI",exam=exam).first()
		result=cutoff.cutoff_by_category.get("General").split("-")[1]
		
		return result
	except:
		return ""
