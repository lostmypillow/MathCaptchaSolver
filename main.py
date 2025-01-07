from MathCaptchaSolver import CaptchaSolver
solver = CaptchaSolver('CaptchaImage1.jpg') # Enter captcha Image path
result = solver.solve_captcha()
print(result[1] if type(result) == list else result)