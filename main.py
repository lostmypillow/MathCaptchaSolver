from MathCaptchaSolver import CaptchaSolver
solver = CaptchaSolver('CaptchaImage2.jpg') # Enter captcha Image path
result = solver.solve_captcha()
print(result)