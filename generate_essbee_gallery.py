import re

with open("/Users/user/.gemini/antigravity/scratch/automateflow-showcase/essbee-realtors.html", "r") as f:
    content = f.read()

gallery_section = """
  <!-- Delivered Projects & Interior Work Showcase Gallery -->
  <section class="bg-white py-16 border-b border-neutral-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="flex flex-col sm:flex-row items-start sm:items-end justify-between gap-4 mb-10">
        <div>
          <span class="text-xs font-semibold tracking-widest text-neutral-500 uppercase">On-Site Portfolio</span>
          <h2 class="text-2xl sm:text-3xl font-bold font-serif-luxury text-neutral-900 mt-1">
            Recent Handover Projects &amp; Walkthroughs
          </h2>
          <p class="text-xs sm:text-sm text-neutral-500 mt-1">Delivered luxury floors across DLF Phase 1, 2, 4 &amp; Sushant Lok, Gurugram</p>
        </div>
        <a href="https://wa.me/918750006668?text=Hello%20Essbee%20Realtors%2C%20please%20share%20video%20walkthroughs%20of%20delivered%20builder%20floors." class="inline-flex items-center gap-1.5 text-xs font-semibold uppercase tracking-wider text-neutral-900 hover:text-neutral-600">
          <span>Request Video Walkthroughs</span>
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/></svg>
        </a>
      </div>

      <!-- 5-Image Curated Catalog Grid -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        
        <!-- Image 1: Living & Drawing Room -->
        <div class="group clean-card rounded-xl overflow-hidden shadow-sm">
          <div class="relative h-64 overflow-hidden bg-neutral-100">
            <img src="https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&w=800&q=80" alt="DLF Phase 2 Living Lounge" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
            <span class="absolute top-3 left-3 bg-neutral-900/85 backdrop-blur-sm text-white text-[10px] font-medium tracking-wider uppercase px-2.5 py-1 rounded">
              DLF Phase 2 • 400 Sq. Yds.
            </span>
          </div>
          <div class="p-4 bg-white">
            <h4 class="font-bold text-sm text-neutral-900 font-serif-luxury">Double-Height Living Lounge</h4>
            <p class="text-xs text-neutral-500 mt-0.5">Bespoke Italian marble, false ceiling lighting &amp; park facing balcony</p>
          </div>
        </div>

        <!-- Image 2: Modular Kitchen -->
        <div class="group clean-card rounded-xl overflow-hidden shadow-sm">
          <div class="relative h-64 overflow-hidden bg-neutral-100">
            <img src="https://images.unsplash.com/photo-1600566753376-12c8ab7fb75b?auto=format&fit=crop&w=800&q=80" alt="Fully Loaded Modular Kitchen" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
            <span class="absolute top-3 left-3 bg-neutral-900/85 backdrop-blur-sm text-white text-[10px] font-medium tracking-wider uppercase px-2.5 py-1 rounded">
              DLF Phase 1 • 500 Sq. Yds.
            </span>
          </div>
          <div class="p-4 bg-white">
            <h4 class="font-bold text-sm text-neutral-900 font-serif-luxury">German Hardware Modular Kitchen</h4>
            <p class="text-xs text-neutral-500 mt-0.5">Pre-fitted with chimney, hob, microwave, baking oven &amp; quartz island</p>
          </div>
        </div>

        <!-- Image 3: Master Bedroom Suite -->
        <div class="group clean-card rounded-xl overflow-hidden shadow-sm">
          <div class="relative h-64 overflow-hidden bg-neutral-100">
            <img src="https://images.unsplash.com/photo-1616594039964-ae9021a400a0?auto=format&fit=crop&w=800&q=80" alt="Master Bedroom Suite" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
            <span class="absolute top-3 left-3 bg-neutral-900/85 backdrop-blur-sm text-white text-[10px] font-medium tracking-wider uppercase px-2.5 py-1 rounded">
              Sushant Lok 1 • 300 Sq. Yds.
            </span>
          </div>
          <div class="p-4 bg-white">
            <h4 class="font-bold text-sm text-neutral-900 font-serif-luxury">Master Bedroom Suite &amp; Wardrobe</h4>
            <p class="text-xs text-neutral-500 mt-0.5">Daikin ductable cooling, wooden flooring accents &amp; walk-in closet</p>
          </div>
        </div>

        <!-- Image 4: Private Terrace Lounge -->
        <div class="group clean-card rounded-xl overflow-hidden shadow-sm sm:col-span-2 lg:col-span-2">
          <div class="relative h-64 overflow-hidden bg-neutral-100">
            <img src="https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=1200&q=80" alt="Private Terrace Garden" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
            <span class="absolute top-3 left-3 bg-neutral-900/85 backdrop-blur-sm text-white text-[10px] font-medium tracking-wider uppercase px-2.5 py-1 rounded">
              Exclusive Terrace Right
            </span>
          </div>
          <div class="p-4 bg-white flex flex-col sm:flex-row sm:items-center justify-between gap-2">
            <div>
              <h4 class="font-bold text-sm text-neutral-900 font-serif-luxury">Half Terrace Garden &amp; Gazebo Lounge</h4>
              <p class="text-xs text-neutral-500 mt-0.5">Allocated with 2nd &amp; 3rd floors, weatherproof wooden deck &amp; sunset view</p>
            </div>
            <a href="https://wa.me/918750006668?text=Hello%20Essbee%20Realtors%2C%20please%20share%20terrace%20floor%20details." class="text-xs font-semibold text-neutral-900 underline whitespace-nowrap">
              Inquire Terrace Floor &rarr;
            </a>
          </div>
        </div>

        <!-- Image 5: Designer Bathrooms -->
        <div class="group clean-card rounded-xl overflow-hidden shadow-sm sm:col-span-2 lg:col-span-1">
          <div class="relative h-64 overflow-hidden bg-neutral-100">
            <img src="https://images.unsplash.com/photo-1584622650111-993a426fbf0a?auto=format&fit=crop&w=800&q=80" alt="Designer Italian Marble Washroom" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
            <span class="absolute top-3 left-3 bg-neutral-900/85 backdrop-blur-sm text-white text-[10px] font-medium tracking-wider uppercase px-2.5 py-1 rounded">
              Kohler &amp; Grohe Fittings
            </span>
          </div>
          <div class="p-4 bg-white">
            <h4 class="font-bold text-sm text-neutral-900 font-serif-luxury">Italian Marble Spa Bathrooms</h4>
            <p class="text-xs text-neutral-500 mt-0.5">Frameless glass partition, wall-hung WC &amp; rain shower fixtures</p>
          </div>
        </div>

      </div>

    </div>
  </section>
"""

# Insert gallery right before "Configurations & Full Inventory Range"
target = "<!-- Configurations & Full Inventory Range -->"
if target in content:
    new_content = content.replace(target, gallery_section + "\n  " + target)
    with open("/Users/user/.gemini/antigravity/scratch/automateflow-showcase/essbee-realtors.html", "w") as f:
        f.write(new_content)
    print("Gallery added successfully!")
else:
    print("Target not found!")
