INSERT INTO "featuredAdventures" (name, location) VALUES
  ('Yellowstone National Park', 'Wyoming, Montana, Idaho, USA'),
  ('Yosemite National Park', 'California, USA'),
  ('Banff National Park', 'Alberta, Canada'),
  ('Kruger National Park', 'Limpopo, South Africa'),
  ('Grand Canyon National Park', 'Arizona, USA'),
  ('Great Smoky Mountains National Park', 'North Carolina, Tennessee, USA'),
  ('Zion National Park', 'Utah, USA'),
  ('Glacier National Park', 'Montana, USA'),
  ('Rocky Mountain National Park', 'Colorado, USA'),
  ('Everglades National Park', 'Florida, USA'),
  ('Arches National Park', 'Utah, USA'),
  ('Acadia National Park', 'Maine, USA'),
  ('Sequoia National Park', 'California, USA')
ON CONFLICT (name) DO NOTHING;