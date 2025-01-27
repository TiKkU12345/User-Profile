import streamlit as st

def main():
    st.title("User Profile")

    # Input fields for user profile
    name = st.text_input("Name")
    email = st.text_input("Email")
    age = st.number_input("Age", min_value=0, max_value=120, step=1)
    bio = st.text_area("Bio")

    # Display user profile
    if st.button("Submit"):
        st.subheader("Profile Information")
        st.write(f"**Name:** **{name}**")
        st.write(f"**Email:** **{email}**")
        st.write(f"**Age:** **{age}**")
        st.write(f"**Bio:** **{bio}**")

if __name__ == "__main__":
    # st.title("UI Profile")
    main()