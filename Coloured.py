import yaml
from graphviz import Digraph

with open("mapping.yaml") as f:
    data = yaml.safe_load(f)

dot = Digraph(format="png")
dot.attr(rankdir="LR")
dot.attr("node", shape="record", style="filled", fontname="Helvetica")

# Assign unique colors here
colors = {
    "customer": "#a2d2ff",
    "orders": "#4895ef",
    "dim_customer": "#fbb1bd",
    "fact_orders": "#fef9b3",
    "dim_customer_profile": "#b8f2e6"
}

schemas = data["schemas"]
relations = data.get("relations", [])

for table, props in schemas.items():
    fields = props["fields"]
    field_lines = [f"{list(f.keys())[0]}: {list(f.values())[0]}" for f in fields]
    label = f"{{{table}|{'\\l'.join(field_lines)}\\l}}"
    dot.node(table, label=label, fillcolor=colors.get(table, "#ffffff"))

for src, dst, label in relations:
    dot.edge(src, dst, label=label)

dot.render("mapping_diagram", view=True)
