def insertion_sort(L):
    if len(L) > 1:
        marker = L.first()
        pivot = L.after(marker)
        while pivot:
            walk = marker
            while walk and walk._element() > pivot._element():
                walk = L.before(walk)
            if walk:
                L.add_after(walk, pivot._element())
            else:
                L.add_first(pivot._element())
            
            L.delete(pivot)
            pivot = L.after(marker)
            if pivot:
                if pivot._element() >= marker._element():
                    marker = pivot
                    pivot = L.after(pivot)
            
            
                