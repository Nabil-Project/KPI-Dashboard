Q_MINMAX_year = """
SELECT MIN(year) AS min_y, MAX(year) AS max_y FROM vgsales
"""

Q_DIM_GENRES = "SELECT DISTINCT genre FROM vgsales ORDER BY genre"
Q_DIM_PLATFORMS = "SELECT DISTINCT platform FROM vgsales ORDER BY platform"
Q_DIM_PUBLISHERS = "SELECT DISTINCT publisher FROM vgsales ORDER BY publisher"

REGIONS = {
    "Global": "global_sales",
    "North America": "na_sales",
    "Europe": "eu_sales",
    "Japan": "jp_sales",
    "Other": "other_sales"
}

def build_where_clause(ymin: int, ymax: int, genre: str, platform: str, publisher: str):
    where = "WHERE year BETWEEN :ymin AND :ymax"
    params = {"ymin": ymin, "ymax": ymax}

    if genre != "All":
        where += " AND genre = :genre"
        params["genre"] = genre

    if platform != "All":
        where += " AND platform = :platform"
        params["platform"] = platform

    if publisher != "All":
        where += " AND publisher = :publisher"
        params["publisher"] = publisher

    return where, params

def q_kpi(where: str, sales_col: str):
    return f"""
    SELECT
      SUM({sales_col}) AS sales,
      COUNT(*) AS nb_rows,
      COUNT(DISTINCT game_name) AS nb_games,
      COUNT(DISTINCT publisher) AS nb_publishers
    FROM vgsales
    {where}
    """

def q_sales_by_year(where: str, sales_col: str):
    return f"""
    SELECT year, SUM({sales_col}) AS sales
    FROM vgsales
    {where}
    GROUP BY year
    ORDER BY year
    """

def q_top_games(where: str, sales_col: str, limit: int = 15):
    return f"""
    SELECT game_name, SUM({sales_col}) AS sales
    FROM vgsales
    {where}
    GROUP BY game_name
    ORDER BY sales DESC
    LIMIT {limit}
    """

def q_top_dim(where: str, sales_col: str, dim: str, limit: int = 15):
    return f"""
    SELECT {dim} AS label, SUM({sales_col}) AS sales
    FROM vgsales
    {where}
    GROUP BY {dim}
    ORDER BY sales DESC
    LIMIT {limit}
    """

