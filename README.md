# pixel_size
Convert magnification setting of stereomicroscopes to absolute pixel size.

## Example

```
from pixel_size import pixel_size

# Calculate physical size of 1 pixel in µm
pixel_size.pixel_size("olympus_mignot", zoom_factor=2.5)
```