import yaml
from graphviz import Digraph

with open("mapping2.yaml") as f:
    data = yaml.safe_load(f)

dot = Digraph(format="png")
dot.attr(rankdir="LR")
dot.attr("node", shape="record", style="filled", fontname="Helvetica")

schemas = data["schemas"]
relations = data.get("relations", [])

for table, props in schemas.items():
    color = props.get("color", "#ffffff")
    fields = props["fields"]
    field_lines = [f"{list(f.keys())[0]}: {list(f.values())[0]}" for f in fields]
    label = f"{{{table}|{'\\l'.join(field_lines)}\\l}}"
    dot.node(table, label=label, fillcolor=color)

for src, dst, label in relations:
    dot.edge(src, dst, label=label)

dot.render("mapping_diagram", view=True)
