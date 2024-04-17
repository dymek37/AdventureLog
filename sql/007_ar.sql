INSERT INTO "worldTravelCountryRegions" (id, name, country_code)
VALUES
  ('AR-C', 'Ciudad Autónoma de Buenos Aires', 'ar'),
  ('AR-B', 'Buenos Aires', 'ar'),
  ('AR-K', 'Catamarca', 'ar'),
  ('AR-H', 'Chaco', 'ar'),
  ('AR-U', 'Chubut', 'ar'),
  ('AR-W', 'Córdoba', 'ar'),
  ('AR-X', 'Corrientes', 'ar'),
  ('AR-E', 'Entre Ríos', 'ar'),
  ('AR-P', 'Formosa', 'ar'),
  ('AR-Y', 'Jujuy', 'ar'),
  ('AR-L', 'La Pampa', 'ar'),
  ('AR-F', 'La Rioja', 'ar'),
  ('AR-M', 'Mendoza', 'ar'),
  ('AR-N', 'Misiones', 'ar'),
  ('AR-Q', 'Neuquén', 'ar'),
  ('AR-R', 'Río Negro', 'ar'),
  ('AR-A', 'Salta', 'ar'),
  ('AR-J', 'San Juan', 'ar'),
  ('AR-D', 'San Luis', 'ar'),
  ('AR-Z', 'Santa Cruz', 'ar'),
  ('AR-S', 'Santa Fe', 'ar'),
  ('AR-G', 'Santiago del Estero', 'ar'),
  ('AR-V', 'Tierra del Fuego', 'ar'),
  ('AR-T', 'Tucumán', 'ar')

ON CONFLICT (id) DO NOTHING;