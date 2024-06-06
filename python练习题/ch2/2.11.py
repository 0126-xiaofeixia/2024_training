#author:dmd
#date:2024.6.1
#功能: 这个程序是一个自动化医疗诊断系统的简化示例，它演示了如何根据输入的症状进行基本的诊断。
def diagnose(symptoms):
    """
    根据症状进行诊断的函数。
    参数:
    symptoms (dict): 患者的症状，以字典形式表示。
    返回:
    str: 可能的疾病诊断。
    """
    if "fever" in symptoms and "cough" in symptoms:
        return "可能是感冒或流感。"
    elif "headache" in symptoms and "nausea" in symptoms:
        return "可能是偏头痛或其他头痛。"
    else:
        return "症状不明确，建议咨询医生。"

# 患者症状示例
patient_symptoms = {"fever": True, "cough": True, "headache": False}
# 进行诊断
print("诊断结果:", diagnose(patient_symptoms))