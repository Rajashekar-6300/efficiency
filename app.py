import streamlit as st

def Tran_Eff(VA, CL, FCL, K, PF):

    Eff = (K * VA * PF)*100 / (K * VA * PF + CL + K**2 * FCL)
    CUL = K**2 * FCL
    return Eff, CUL
st.title("Transformer Efficiency and Copper Loss Calculator")
st.header("Calculate Transformer Efficiency and Copper Losses at Various Loads")

VA = st.number_input("Enter Rating of Transformer (VA)", min_value=0.0, step=1.0)
CL = st.number_input("Enter Core Losses (CL) in Watts", min_value=0.0, step=1.0)
FCL = st.number_input("Enter Full Load Copper Losses (FCL) in Watts", min_value=0.0, step=1.0)
K = st.number_input("Enter Loading on Transformer (K)", min_value=0.0, max_value=1.0, step=0.01)
PF = st.number_input("Enter Power Factor (PF)", min_value=0.0, max_value=1.0, step=0.01)

if st.button("Compute"):
    if VA > 0 and CL > 0 and FCL > 0 and 0 <= K <= 1 and 0 <= PF <= 1:
        Eff, CUL = Tran_Eff(VA, CL, FCL, K, PF)
        st.write("Transformer Efficiency: {:.2f}%".format(Eff))
        st.write("Copper Losses: {:.2f} Watts".format(CUL))
    else:
        st.error("Invalid inputs. Ensure all values are in the correct range.")