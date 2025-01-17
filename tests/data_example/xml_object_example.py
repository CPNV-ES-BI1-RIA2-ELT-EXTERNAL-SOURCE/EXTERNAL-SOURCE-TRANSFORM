def get_xml_object_example():
    return '''<data>
  <stop>
    <id>8501120</id>
    <name>Lausanne</name>
    <type>train,strain</type>
    <x>537875</x>
    <y>152042</y>
    <lon>6.629087</lon>
    <lat>46.516795</lat>
  </stop>
  <connections>
    <connection>
      <time>2024-01-12 00:02:00</time>
      <G>R</G>
      <L>4</L>
      <Z>024492</Z>
      <type>train</type>
      <line>R</line>
      <operator>SBB</operator>
      <color>039~fff~</color>
      <type_name>Railway</type_name>
      <terminal>
        <id>8501103</id>
        <name>Vallorbe</name>
        <x>518333</x>
        <y>174024</y>
        <lon>6.370564</lon>
        <lat>46.712419</lat>
      </terminal>
      <track>81DG</track>
      <subsequent_stops>
        <stop>
          <id>8518452</id>
          <name>Prilly-Malley</name>
          <x>535856</x>
          <y>153164</y>
          <lon>6.602624</lon>
          <lat>46.526697</lat>
          <arr>1970-01-01 00:05:00</arr>
          <dep>1970-01-01 00:06:00</dep>
        </stop>
        <stop>
          <id>8501118</id>
          <name>Renens VD</name>
          <x>534051</x>
          <y>154334</y>
          <lon>6.578933</lon>
          <lat>46.537046</lat>
          <arr>1970-01-01 00:08:00</arr>
          <dep>1970-01-01 00:08:00</dep>
        </stop>
        <stop>
          <id>8501117</id>
          <name>Bussigny</name>
          <x>531985</x>
          <y>155530</y>
          <lon>6.551827</lon>
          <lat>46.547598</lat>
          <arr>1970-01-01 00:11:00</arr>
          <dep>1970-01-01 00:11:00</dep>
        </stop>
      </subsequent_stops>
    </connection>
  </connections>
  <request>null</request>
  <eof>1</eof>
</data>
'''