import streamlit as st
import pandas as pd
import os
import glob

st.title("YouTube Big Data Analytics Dashboard")
st.write("Results generated using Hadoop + Spark")


def load_folder(folder):
    files = glob.glob(os.path.join(folder, "*.csv"))

    df_list = []

    for file in files:
        try:
            df = pd.read_csv(file, engine="python", on_bad_lines="skip")
            df_list.append(df)
        except:
            pass

    if df_list:
        return pd.concat(df_list, ignore_index=True)

    return None


# -------- Top Viewed --------
if os.path.exists("results/top_views"):
    st.header("Top Viewed Videos")
    df = load_folder("results/top_views")
    if df is not None:
        st.dataframe(df.head(10))


# -------- Top Likes --------
if os.path.exists("results/top_likes"):
    st.header("Top Liked Videos")
    df = load_folder("results/top_likes")
    if df is not None:
        st.dataframe(df.head(10))


# -------- Top Comments --------
if os.path.exists("results/top_comments"):
    st.header("Top Commented Videos")
    df = load_folder("results/top_comments")
    if df is not None:
        st.dataframe(df.head(10))


# -------- Channel Views --------
if os.path.exists("results/channel_views"):
    st.header("Channel Total Views")
    df = load_folder("results/channel_views")
    if df is not None:
        st.dataframe(df.head(10))


# -------- Category Count --------
if os.path.exists("results/category_count"):
    st.header("Category Distribution")
    df = load_folder("results/category_count")
    if df is not None:
        st.bar_chart(df.set_index(df.columns[0]))


# -------- Average Views --------
if os.path.exists("results/avg_views"):
    st.header("Average Views by Channel")
    df = load_folder("results/avg_views")
    if df is not None:
        st.dataframe(df.head(10))


# -------- Trending --------
if os.path.exists("results/trending"):
    st.header("Trending Videos")
    df = load_folder("results/trending")
    if df is not None:
        st.dataframe(df.head(10))


st.success("Dashboard powered by Hadoop + Spark")
