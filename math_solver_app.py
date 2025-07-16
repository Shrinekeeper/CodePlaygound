import streamlit as st
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr

def solve_expression(expr_str):
    try:
        x, y, z = sp.symbols('x y z')

        # Check for equation
        if '=' in expr_str:
            lhs, rhs = expr_str.split('=')
            expr = sp.Eq(parse_expr(lhs.strip()), parse_expr(rhs.strip()))
        else:
            expr = parse_expr(expr_str)

        # Solve or evaluate
        if isinstance(expr, sp.Equality):
            solution = sp.solve(expr, x)
            return f"🧮 Solution: {solution}"
        
        elif 'diff' in expr_str:
            return f"📘 Differentiated: {sp.diff(expr, x)}"
        
        elif 'integrate' in expr_str:
            return f"📗 Integrated: {sp.integrate(expr, x)}"
        
        elif 'limit' in expr_str:
            return f"📙 Limit: {sp.limit(expr, x, 0)}"
        
        else:
            simplified = sp.simplify(expr)
            return f"📄 Simplified: {simplified}"

    except Exception as e:
        return f"❌ Error: {e}"

# Streamlit UI
st.set_page_config(page_title="JEE Math Solver", page_icon="🧮")
st.title("🧮JEE Advanced Math Solver")

st.markdown("Type an equation or math expression below (e.g. `x**2 - 4 = 0`, `diff(x**2)`, `integrate(x**2 + 1)`, `limit(sin(x)/x, x, 0)`)")

user_input = st.text_input("🔢 Enter expression or equation:")

if user_input:
    result = solve_expression(user_input)
    st.markdown(f"### ➤ {result}")
