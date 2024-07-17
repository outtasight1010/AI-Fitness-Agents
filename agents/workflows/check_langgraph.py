try:
    from langgraph import Graph, Node
    print("Graph and Node classes are available.")
except ImportError as e:
    print("ImportError:", e)
