from collections import deque

def graph(project):
    g={device:set() for device in project.get('devices',{})}
    for link in project.get('links',[]):
        a=link['endpoint_a']['device']; b=link['endpoint_b']['device']
        if a in g and b in g: g[a].add(b); g[b].add(a)
    return g

def shortest_path(project,start,end):
    g=graph(project); queue=deque([(start,[start])]); seen={start}
    while queue:
        node,path=queue.popleft()
        if node==end:return path
        for neighbor in g.get(node,[]):
            if neighbor not in seen:
                seen.add(neighbor);queue.append((neighbor,path+[neighbor]))
    return None
