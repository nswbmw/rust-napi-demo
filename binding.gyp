{
  'variables': {
    'base_cflags': [
      '-Wall',
      '-Wextra',
      '-Wno-unused-parameter',
      '-std=c11',
    ],
    'debug_cflags': ['-g', '-O0'],
    'release_cflags': ['-O3'],
  },
  'targets': [
    {
      'target_name': 'example',
      'sources': ['src/binding.c'],
      'conditions': [
        ['OS == "win"', {
          'libraries': [
            '../target/release/napi_demo.lib',
            'advapi32.lib',
            'ws2_32.lib',
            'userenv.lib',
            'shell32.lib',
          ],
        }, {
          'libraries': [
            '../target/release/libnapi_demo.a',
          ],
        }],
      ],
      'configurations': {
        'Debug': {
          'cflags': ['<@(debug_cflags)'],
          'xcode_settings': {
            'OTHER_CFLAGS': ['<@(debug_cflags)'],
          },
        },
        'Release': {
          'cflags': ['<@(release_cflags)'],
          'xcode_settings': {
            'OTHER_CFLAGS': ['<@(release_cflags)'],
          },
        },
      },
      'cflags': ['<@(base_cflags)'],
      'xcode_settings': {
        'OTHER_CFLAGS': ['<@(base_cflags)'],
      },
    },
  ],
}