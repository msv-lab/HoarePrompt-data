N=raw_input()
a=raw_input().split()

import numpy as np
ans=np.abs(np.max(a)-np.min(a))
print(ans)